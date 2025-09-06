from flask import Flask, render_template, request, session, redirect, url_for
from app.components.retriever import create_qa_chain
from dotenv import load_dotenv
import os

from langchain.schema import HumanMessage


load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")


app = Flask(__name__)
app.secret_key = os.urandom(24)

from markupsafe import Markup

def nl2br(text: str) -> str:
    """Convert newlines in text to HTML line breaks."""
    return Markup(text.replace("\n", "<br>\n"))

app.jinja_env.filters['nl2br'] = nl2br

@app.route("/", methods=["GET", "POST"])

def index():
    if "messages" not in session:
        session["messages"] = []
    if request.method == "POST":
        user_input = request.form.get("prompt")

        if user_input:
            messages = session["messages"]
            messages.append({"role":"user", "content":user_input})
            session["messages"] = messages

            try:
                qa_chain = create_qa_chain()

                chat_history = []
                for i in range(0, len(messages)-1,2):
                    if messages[i]["role"] == "user" and messages[i+1]["role"]=="assistant":
                        chat_history.append((messages[i]["content"], messages[i+1]["content"]))
                
                response = qa_chain.invoke({
                    "question": user_input,
                    "chat_history": chat_history
                })

                result = response.get("answer", response.get("result","No response"))



                messages.append({"role": "assistant", "content": result})
                session["messages"] = messages

                print("HERE",chat_history)
            
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                return render_template("index.html", messages=session["messages"], error=error_msg)

        return redirect(url_for("index"))
    return render_template("index.html", messages=session["messages"])

@app.route("/clear")
def clear():
    session.pop("messages", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 5000, debug=False, use_reloader = False)