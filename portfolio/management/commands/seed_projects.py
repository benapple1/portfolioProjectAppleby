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
        "title": "Machine Learning Project using scikit-learn",
        "summary": "[REPLACE WITH YOUR ONE-SENTENCE SUMMARY] Example: I trained a scikit-learn model to make predictions from a dataset and explain the results in business language.",
        "business_problem": "[REPLACE WITH THE REAL DATA PROBLEM] Explain what decision the model supports, who would use the prediction, and why the result matters.",
        "tools_used": "[REPLACE WITH YOUR ACTUAL TOOLS] Example: Python, pandas, scikit-learn, train-test split, accuracy score, confusion matrix, Jupyter Notebook.",
        "key_features": "[REPLACE WITH YOUR REAL FEATURES]\nFeature 1: Describe the dataset and target variable.\nFeature 2: Describe cleaning, feature selection, or model training.\nFeature 3: Describe the metric or evaluation result.\nInterview talking point: Explain what the model result means and what its limitations are.",
        "role_contribution": "[REPLACE WITH WHAT YOU PERSONALLY DID] Mention how you prepared the data, trained the model, evaluated performance, and explained the result.",
        "biggest_challenge": "[REPLACE WITH YOUR BIGGEST CHALLENGE] Example: cleaning data, choosing features, understanding model metrics, or avoiding overfitting.",
        "lessons_learned": "[REPLACE WITH WHAT YOU LEARNED] Focus on data preparation, fair evaluation, model limitations, and communicating technical results clearly.",
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


class Command(BaseCommand):
    help = "Seed the portfolio with the six required AI course projects."

    def handle(self, *args, **options):
        for project in PROJECTS:
            Project.objects.update_or_create(
                title=project["title"],
                defaults=project,
            )
        self.stdout.write(self.style.SUCCESS(f"Seeded {len(PROJECTS)} projects."))
