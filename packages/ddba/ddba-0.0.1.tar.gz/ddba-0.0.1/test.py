import openai
import json


# print(openai.Model.list())


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_password():
    return json.dumps({
        "password": "123456"
    })


def get_max_connections():
    return json.dumps({
        "max_connections": 100
    })


def show_my_abilities():
    return json.dumps({
        "abilities": ["get_password", "set_password"]
    })


def set_password(new_password):
    if new_password is None or new_password == "":
        return json.dumps({
            "success": False,
            "error": "Password cannot be empty"
        })
    return json.dumps({
        "success": True,
    })


def set_max_connections(max_connections):
    return json.dumps({
        "success": True,
    })


def run_conversation():
    model = "gpt-3.5-turbo-0613"
    print("using  model: " + model)

    # Step 1: send the conversation and available functions to GPT
    messages = [{"role": "system", "content": "You are a professional DBA.你必须用中文对话"}]
    # messages = []
    # messages.append({"role": "user", "content": "你当前有哪些功能？"})
    # print(messages)
    functions = [
        {
            "name": "set_password",
            "description": "Update the password for a database user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "new_password": {
                        "type": "string",
                        "description": "The new password for the database, new password cannot be empty.",
                    }
                },
                "required": ["new_password"]
            }
        },
        {
            "name": "get_password",
            "description": "Retrieve the password for a database user",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "show_my_abilities",
            "description": "Display my abilities and skills",
            "parameters": {
                "type": "object",
                "properties": {

                },
                "required": []
            }
        },
        {
            "name": "set_max_connections",
            "description": "Update the maximum number of connections for a database user.",
            "parameters": {
                "type": "object",
                "properties": {
                    "max_connections": {
                        "type": "integer",
                        "description": "The maximum number of connections for the database, max connections cannot be empty.",
                    }
                },
                "required": ["max_connections"]
            }
        },
        {
            "name": "get_max_connections",
            "description": "Retrieve the maximum number of connections.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }

    ]

    #
    question = input("User: ")
    messages.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            functions=functions,
            function_call="auto",  # auto is default, but we'll be explicit
    )

    while True:
        response_message = response["choices"][0]["message"]
        if response_message.get("function_call"):
            # Step 3: call the function
            # Note: the JSON response may not always be valid; be sure to handle errors
            available_functions = {
                "set_password": set_password,
                "get_password": get_password,
                "show_my_abilities": show_my_abilities,
                "set_max_connections": set_max_connections,
                "get_max_connections": get_max_connections
            }  # only one function in this example, but you can have multiple
            function_name = response_message["function_call"]["name"]
            function_to_call = available_functions[function_name]
            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = function_to_call(**function_args)
            print(f"[function_call] {function_name}{function_args} returned: {function_response}")

            # Step 4: send the info on the function call and function response to GPT
            messages.append(response_message)  # extend conversation with assistant's reply
            messages.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                functions=functions,
                function_call="auto",
            )  # get a new response from GPT where it can see the function response
            # return second_response["choices"][0]["message"]["content"]
        else:
            print(response_message["content"])
            messages.append(response_message)  # extend conversation with assistant's reply
            messages.append(
                {
                    "role": "user",
                    "content": input("User:"),
                }
            )  # extend conversation with function response
            print(messages)
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                functions=functions,
                function_call="auto",  # auto is default, but we'll be explicit
            )


print(run_conversation())
