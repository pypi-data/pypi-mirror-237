# coding: utf-8
import os
import requests
from .utils import check_email
from .exceptions import ApiException, AuthenticationFailed, NotLoggedInException

DEBUG = os.getenv("DEBUG", False)
BASE_URL = os.getenv("TAGONE_BASE_URL")


class TagoneClient:
    def __init__(self, cookie=None):
        if DEBUG:
            print("init called")

        if not BASE_URL:
            raise ValueError("TAGONE_BASE_URL não configurada")

        self.session = requests.Session()
        if cookie:
            self.set_cookie(cookie)

    def set_cookie(self, cookie):
        if DEBUG:
            print("set_cookie called: cookie set?", cookie is not None)
        if cookie:
            self.session.cookies.set("TagOneCookie", cookie)
        else:
            self.session.cookies.clear()

    def get_cookie(self):
        return self.session.cookies.get("TagOneCookie")

    def do_login(self, username, password):
        """
        Faz login com TagOne
        Se usuário não existe, é incluído ao fazer login.
        """
        if DEBUG:
            print('do_login called with username="{}"'.format(username))
        username = username.upper()
        url = f"{BASE_URL}/Usuario/Login(UserName='{username}',PassWord='{password}',Remember=true)"
        if DEBUG:
            print("url:", url)
        resp = self.session.get(url)
        if resp.status_code == 400:
            print("auth failed, status_code:", resp.status_code)
            raise AuthenticationFailed(f"Usuário ou senha inválidos!")
        if resp.status_code != 200:
            print("auth failed, status_code:", resp.status_code)
            print(resp.text)
            raise ApiException("Erro desconhecido ao autenticar no TagOne")

        return self.get_user_data()

    def get_user_data(self):
        if DEBUG:
            print("get_user_data called")

        url = f"{BASE_URL}/Usuario/GetLoggedClaims"
        claims = {
            "username": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
            "empresas": "Empresas",
            "empresa_padrao": "EmpresaPadrao",
            "nome": "FullName",
            "email": "Email",
            "codigo_perfil": "Perfil",
        }
        resp = self.session.get(url)
        if resp.status_code == 401:
            self.set_cookie(None)
            raise NotLoggedInException("Autorização negada, faça login no TagOne")
        if resp.status_code != 200:
            print("auth failed, status_code:", resp.status_code)
            print(resp.text)
            raise ApiException("Erro desconhecido ao consultar no TagOne")

        logged_claims = resp.json()

        # usa claims do tagone e converte em um dict
        self.user_data = dict(
            [(field, logged_claims["Values"][logged_claims["Keys"].index(key)]) for field, key in claims.items()]
        )
        self.user_data["username"] = self.user_data["username"].upper()
        self.user_data["empresa_padrao"] = int(self.user_data["empresa_padrao"])
        self.user_data["empresas"] = [int(e) for e in self.user_data["empresas"].split(",")]
        if not check_email(self.user_data["email"]):
            self.user_data["email"] = None

        return self.user_data

    def do_logout(self):
        self.set_cookie(None)
        self.user_data = None

    def request(self, url: str, method: str = "GET", payload: dict = None):
        if DEBUG:
            print(f"{method} {BASE_URL + url} {payload or ''}")
        url = url.replace("    ", "").replace("\n", "")
        if method == "GET":
            resp = self.session.get(BASE_URL + url)
        elif method == "POST":
            resp = self.session.post(BASE_URL + url, json=payload)
        elif method == "DELETE":
            resp = self.session.delete(BASE_URL + url, json=payload)
        else:
            raise Exception(f"Method {method} not implemented")
        try:
            data = resp.json()
        except:
            return resp.text
        return data["value"] if "value" in data else data

    def tagone_get(self, url):
        return self.request("GET", url)

    def tagone_post(self, url, payload):
        return self.request("POST", url, payload)

    def tagone_delete(self, url, payload):
        return self.request("DELETE", url, payload)


# def tagone_upload_anexo(codigo_produto: int, content: anvil.BlobMedia):
#     print("tagone_upload_anexo called")
#     client = TagoneClient()

#     payload = {"CodigoProduto": codigo_produto, "Observacao": "", "CodigoAnexoTipo": 1}

#     files = {
#         "Anexo": (None, json.dumps(payload), "application/json"),
#         "file": (content.name, content.get_bytes(), "application/octet-stream"),
#     }

#     resp = client.session.post(client.BASE_URL + "/Anexo/Upload", files=files)

#     try:
#         data = resp.json()
#     except:
#         return resp.text
#     return data["value"] if "value" in data else data
