from django.core.management.base import BaseCommand

from portfolio.models import Project

PROJECTS = [
    {
        "title": "Chatbot Project",
        "summary": "[REPLACE WITH YOUR ONE-SENTENCE SUMMARY] Example: I built a chatbot prototype that answers common questions and shows how prompt design can support faster customer or student support.",
        "business_problem": "[REPLACE WITH THE REAL PROBLEM YOUR CHATBOT SOLVES] Explain who the user is, what repeated question or support issue they have, and why an AI chatbot would create business or campus value.",
        "tools_used": "[REPLACE WITH YOUR ACTUAL TOOLS] Example: Python, prompt engineering, OpenAI API concepts, Streamlit or notebook, test prompts.",
        "key_features": "[REPLACE WITH YOUR REAL FEATURES]\nFeature 1: Describe the main chatbot function.\nFeature 2: Describe how the chatbot handles unclear questions.\nFeature 3: Describe any prompt, memory, evaluation, or user interface feature.\nInterview talking point: Explain how these features improve speed, consistency, or user experience.",
        "role_contribution": "[REPLACE WITH WHAT YOU PERSONALLY DID] Mention how you planned the use case, wrote prompts, tested responses, revised the flow, and prepared the project for presentation.",
        "biggest_challenge": "[REPLACE WITH YOUR BIGGEST CHALLENGE] Example: keeping the chatbot helpful while preventing off-topic or unreliable answers.",
        "lessons_learned": "[REPLACE WITH WHAT YOU LEARNED] Focus on prompt iteration, testing, guardrails, user needs, and explaining AI limitations in a professional way.",
        "github_link": "",
        "demo_link": "",
        "category": "agent",
    },
    {
        "title": "n8n Agent Workflow Project",
        "summary": "[REPLACE WITH YOUR ONE-SENTENCE SUMMARY] Example: I created an n8n workflow that uses AI to automate a repeated business task from trigger to follow-up.",
        "business_problem": "[REPLACE WITH THE REAL WORKFLOW PROBLEM] Explain the manual process, who loses time, what gets delayed, and how automation could improve consistency or productivity.",
        "tools_used": "[REPLACE WITH YOUR ACTUAL TOOLS] Example: n8n, webhook trigger, AI agent node, Gmail/Slack/Sheets integration, API request, test data.",
        "key_features": "[REPLACE WITH YOUR REAL FEATURES]\nFeature 1: Describe the trigger that starts the workflow.\nFeature 2: Describe the AI decision or classification step.\nFeature 3: Describe the automated action or notification.\nInterview talking point: Explain where automation saves time or reduces errors.",
        "role_contribution": "[REPLACE WITH WHAT YOU PERSONALLY DID] Mention how you designed the process, configured nodes, tested sample inputs, and documented the workflow.",
        "biggest_challenge": "[REPLACE WITH YOUR BIGGEST CHALLENGE] Example: handling incomplete input, connecting tools correctly, or debugging workflow steps.",
        "lessons_learned": "[REPLACE WITH WHAT YOU LEARNED] Focus on process mapping, workflow testing, API thinking, and connecting AI automation to business value.",
        "github_link": "",
        "demo_link": "",
        "category": "automation",
    },
    {
        "title": "LangChain Agent Project",
        "summary": "[REPLACE WITH YOUR ONE-SENTENCE SUMMARY] Example: I built a LangChain agent prototype that uses tools or context to answer a task-focused question more effectively than a basic chatbot.",
        "business_problem": "[REPLACE WITH THE REAL PROBLEM YOUR AGENT ADDRESSES] Explain why a user would need an agent, what information or tool use is required, and what value the agent creates.",
        "tools_used": "[REPLACE WITH YOUR ACTUAL TOOLS] Example: Python, LangChain, prompt templates, retriever, tool calling, notebook, environment variables.",
        "key_features": "[REPLACE WITH YOUR REAL FEATURES]\nFeature 1: Describe what the agent can do.\nFeature 2: Describe the tool, retriever, or context it uses.\nFeature 3: Describe the output format or testing approach.\nInterview talking point: Explain why an agent was useful for this problem.",
        "role_contribution": "[REPLACE WITH WHAT YOU PERSONALLY DID] Mention how you built the chain or agent, tested prompts, selected tools, and evaluated the results.",
        "biggest_challenge": "[REPLACE WITH YOUR BIGGEST CHALLENGE] Example: keeping the agent predictable, debugging tool calls, or understanding LangChain components.",
        "lessons_learned": "[REPLACE WITH WHAT YOU LEARNED] Focus on agent design, tool use, evaluation, and when an AI agent is better than a simpler solution.",
        "github_link": "",
        "demo_link": "",
        "category": "agent",
    },
    {
        "title": "Google AI Studio Media Project",
        "summary": "[REPLACE WITH YOUR ONE-SENTENCE SUMMARY] Example: I used Google AI Studio to create or analyze media content for a communication, presentation, or marketing-style use case.",
        "business_problem": "[REPLACE WITH THE REAL MEDIA PROBLEM] Explain the audience, message, or communication need, and why AI-generated or AI-assisted media would help.",
        "tools_used": "[REPLACE WITH YOUR ACTUAL TOOLS] Example: Google AI Studio, Gemini, image or video prompt, multimodal input, prompt revisions.",
        "key_features": "[REPLACE WITH YOUR REAL FEATURES]\nFeature 1: Describe the type of media or prompt you created.\nFeature 2: Describe how you revised or compared outputs.\nFeature 3: Describe how you judged quality and usefulness.\nInterview talking point: Explain how AI supported creativity while still requiring human review.",
        "role_contribution": "[REPLACE WITH WHAT YOU PERSONALLY DID] Mention how you wrote prompts, selected outputs, refined the message, and connected the result to an audience or business goal.",
        "biggest_challenge": "[REPLACE WITH YOUR BIGGEST CHALLENGE] Example: getting the output to match the intended tone, audience, or visual direction.",
        "lessons_learned": "[REPLACE WITH WHAT YOU LEARNED] Focus on prompt clarity, audience fit, brand/message constraints, and responsible review of AI media.",
        "github_link": "",
        "demo_link": "",
        "category": "media",
    },
    {
        "title": "Machine Learning Project: Predictive Modeling with scikit-learn",
        "summary": "A collection of beginner machine learning exercises using scikit-learn to practice regression, classification, model evaluation, and data visualization.",
        "business_problem": "Many business decisions depend on identifying patterns in data and using those patterns to make informed predictions. This project focused on learning how machine learning models can be used to analyze structured datasets, evaluate model performance, and communicate results in a way that supports decision-making.",
        "tools_used": "Python, scikit-learn, pandas, matplotlib, seaborn, NumPy",
        "key_features": "Built regression models using datasets such as Auto MPG and California Housing.\nUsed linear regression to compare predicted outcomes against actual values.\nCreated scatterplots and actual vs. predicted visualizations to evaluate model fit.\nBuilt a KNN classification model using the Iris dataset.\nEvaluated classification performance with predicted vs. expected labels and a confusion matrix.\nPracticed train/test splitting, model fitting, prediction, and basic model evaluation.",
        "role_contribution": "I wrote and ran the Python scripts for each machine learning exercise, loaded and prepared datasets, trained models, generated predictions, and created visualizations to evaluate results. My main focus was not just getting the code to run, but understanding what the model output meant and how to explain it clearly.",
        "biggest_challenge": "The biggest challenge was connecting the technical output to a clear interpretation. It was one thing to train a model or produce a plot, but the more important step was understanding what the results showed, whether the model performed well, and how to communicate that without overcomplicating it.",
        "lessons_learned": "This project helped me better understand the basic machine learning workflow: prepare the data, split it into training and testing sets, train a model, generate predictions, and evaluate the results. I also learned the difference between regression and classification problems and became more comfortable using visualizations to explain model performance.\n\nDemo note: This project was completed through local Python scripts and visual outputs. Screenshots of model results and plots are included as project visuals.",
        "github_link": "",
        "demo_link": "",
        "category": "machine-learning",
    },
    {
        "title": "Campus SkillSwap Django Project",
        "summary": "A Django-based marketplace that allows students to post, discover, and exchange skills and services within a campus community.",
        "business_problem": "Students often have valuable skills they could offer, but there is no simple, centralized way to connect with others who need those skills. Without a structured system, these opportunities are informal, hard to discover, and difficult to manage. This project explores how a simple platform could make peer-to-peer skill exchange more accessible and organized.",
        "tools_used": "Django, Python, SQLite, Bootstrap, HTML/CSS, GitHub Copilot",
        "key_features": "User registration, login, and logout.\nSkill posts with title, description, category, price/free option, contact preference, availability status, and owner.\nCreate, edit, and delete functionality for user skill posts.\nDashboard view for users to manage their own listings.\nSearch functionality by title or category.\nReview and rating system for feedback.\nBooking/request system for connecting users.",
        "role_contribution": "I built this project end-to-end using Django, working through the full development process from setting up models and views to building templates and user flows. I used GitHub Copilot as a support tool, but focused on understanding how each component worked, including how models connect to users, how views handle logic, and how templates render dynamic content.",
        "biggest_challenge": "One of the biggest challenges was understanding how all parts of a Django application connect, especially linking the Skill model to users and managing CRUD functionality across multiple views. It took time to understand how data flows from the database through views and into templates, and how to structure that cleanly without breaking functionality.",
        "lessons_learned": "This project helped me understand how a full web application is structured and how backend logic connects to what users see. More importantly, it reinforced how to break a larger system into smaller, manageable pieces and build them step by step. I also became more comfortable using tools like Copilot productively while still making sure I understood the underlying logic.\n\nDemo note: This project runs locally as a Django application.",
        "github_link": "https://github.com/benapple1/campus_skillswap",
        "demo_link": "",
        "category": "web-app",
    },
]

PROJECT_TITLE_ALIASES = {
    "Machine Learning Project: Predictive Modeling with scikit-learn": "Machine Learning Project using scikit-learn",
}


class Command(BaseCommand):
    help = "Seed the portfolio with the six required AI course projects."

    def handle(self, *args, **options):
        for project in PROJECTS:
            old_title = PROJECT_TITLE_ALIASES.get(project["title"])
            existing_project = None
            if old_title:
                existing_project = Project.objects.filter(title=old_title).first()

            if existing_project:
                for field, value in project.items():
                    setattr(existing_project, field, value)
                existing_project.slug = ""
                existing_project.save()
            else:
                Project.objects.update_or_create(
                    title=project["title"],
                    defaults=project,
                )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(PROJECTS)} projects."))
