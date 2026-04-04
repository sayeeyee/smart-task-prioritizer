import gradio as gr
from env import TaskEnv
from models import Action

env = TaskEnv()


gtake_theme_css = """

body, .gradio-container { 
    background: radial-gradient(circle at 20% 30%, #1e293b 0%, #0b0f19 70%, #070a11 100%) !important;
    color: #ffffff !important;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
}


h1, h2, .status-text { 
    background: linear-gradient(90deg, #ffffff 0%, #3b82f6 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}


.form { 
    background: rgba(255, 255, 255, 0.04) !important; 
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 24px !important;
    padding: 30px !important;
    backdrop-filter: blur(12px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}


.gr-radio-container {
    display: flex;
    gap: 12px;
}
label.gr-radio-label { 
    background: rgba(255, 255, 255, 0.05) !important; 
    color: #94a3b8 !important; 
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 50px !important; /* High curves as requested */
    padding: 10px 20px !important;
    transition: all 0.3s ease;
}
label.selected { 
    background: #2563eb !important; 
    color: white !important;
    border-color: #3b82f6 !important;
    box-shadow: 0 0 15px rgba(37, 99, 235, 0.5);
    
}


button.primary {
    background: linear-gradient(90deg, #1e40af, #3b82f6) !important;
    border: none !important;
    font-weight: bold !important;
    box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
    text-transform: uppercase;
    letter-spacing: 1px;
}
button.primary:hover {
    box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
    transform: translateY(-1px);
    
}


textarea { 
    background: rgba(0, 0, 0, 0.3) !important; 
    color: #121112 !important; 
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    border-radius: 20px !important;
    padding: 15px !important;
}

/
p, .gr-form-label {
    color: #94a3b8 !important;
}
"""

def run_task(priority):
    task = env.reset()
    action = Action(priority=priority)
    result = env.step(action)

    output = f"""
[ SYSTEM LOG ]
-----------------------------------------
TASK: {task.description}
DEADLINE: {task.deadline}
IMPORTANCE: {task.importance}

RESULT: {"SUCCESS" if result.correct else "FAILED"}
PRIORITY APPLIED: {priority.upper()}
REWARD EARNED: {result.reward}
"""
    return output


iface = gr.Interface(
    fn=run_task,
    inputs=gr.Radio(["low", "medium", "high"], label="Select Priority Level"),
    outputs="text",
    title="Smart Task Prioritizer",

    css=gtake_theme_css
)

iface.launch()
       