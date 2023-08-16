from pytest_bdd import scenario, given, when, then, parsers
from src.schemas.user import UserDB
from src.api.users import database as db

@scenario(
    scenario_name="Login bem sucedido de um usuário",
    feature_name="../features/login.feature"
)
def test_successful_login(): # testar o login bem sucedido de um usuário
    pass

@given(
    parsers.cfparse(
        'um usuário com id "{user_id}" e e-mail "{user_email}" e senha "{user_password}" está cadastrado no sistema'
    )
)
def mock_user_in_database(user_id: str, user_email: str, user_password: str): # adiciona o usuário na base de dados (condição anterior ao teste)
    db.append(UserDB(
        id=int(user_id),
        name="Nome",
        surname="Sobrenome",
        email=user_email,
        birthdate="2000-01-01",  
        plan=True,
        passwd=user_password
    ))

@when(
    parsers.cfparse(
        'o usuário envia uma requisição POST para "{login_url}" com e-mail "{user_email}" e senha "{user_password}"'
    ),
    target_fixture="context"
)
def send_login_request(client, context, login_url: str, user_email: str, user_password: str):

    response = client.post(login_url, data={"username": user_email, "password": user_password}) # envia um post para a rota de login com o email e senha do usuário
    context["response"] = response
    return context

@then(parsers.cfparse('o status da resposta deve ser "{status_code}"'), target_fixture="context")
def check_login_response_status_code(context, status_code: str):


    assert context["response"].status_code == int(status_code) # verifica se o código de status da resposta é 200
    return context

@then(
    parsers.cfparse(
        'o JSON da resposta deve conter um token de acesso válido com o valor "{user_id}" e tipo "{token_type}"'
    ),
    target_fixture="context"
)
def check_login_response_contains_token(context, user_id: str, token_type: str):
    
    expected_token_response = {"access_token": user_id, "token_type": token_type} # verifica se o JSON da resposta contém um token equivalente ao id do usuário e se o tipo do token é bearer
    assert context["response"].json() == expected_token_response
    return context
