from django.core.management.base import BaseCommand

from portfolio.models import Project

PROJECTS = [
    {
        "title": "n8n Multi-Agent Handyman Workflow Project",
        "summary": "Built a multi-agent business workflow in n8n that simulates an automated handyman operations desk using Gemini-powered agents and workflow orchestration.",
        "business_problem": "Small service businesses often spend significant time manually handling customer intake, pricing estimates, scheduling, and communication. This project explored how a multi-agent AI workflow could automate much of that operational process by routing customer requests through specialized agents that each handle a different business function.",
        "tools_used": "n8n Cloud, Google Gemini API, JavaScript, HTTP Requests, Webhooks, Prompt Engineering",
        "key_features": "Multi-agent workflow orchestration.\nAI-powered customer intake extraction.\nRules-based pricing estimation.\nScheduling workflow using external time APIs.\nAutomated customer communication drafting.\nWebhook-based workflow triggers.\nJSON parsing and validation handling.\nInter-agent communication through HTTP requests.",
        "role_contribution": "I built and configured the multi-agent workflow structure inside n8n using drag-and-drop automation nodes, HTTP requests, JavaScript logic, and Gemini integrations. I worked through how agents communicate with one another, how structured JSON outputs are passed between workflows, and how orchestration logic can automate a multi-step business process.",
        "biggest_challenge": "One of the biggest challenges was handling structured JSON outputs reliably between workflows, especially when Gemini responses occasionally returned invalid formatting or markdown-wrapped JSON. Managing data flow between agents and debugging webhook payloads also required careful testing and iteration.",
        "lessons_learned": "This project helped me better understand how multi-agent systems can coordinate specialized tasks inside a larger automation pipeline. I also gained experience working with workflow orchestration, API integrations, structured AI outputs, and business process automation using low-code tools.",
        "github_link": "https://github.com/benapple1/Handyman2.git",
        "demo_link": "",
        "category": "automation",
    },
    {
        "title": "LangChain Agent Project",
        "summary": "Built a conversational AI chatbot using LangChain and Google Gemini that processes user prompts and generates responses through a structured LLM workflow.",
        "business_problem": "Many AI tools feel disconnected from how real users naturally interact with systems. This project explored how conversational interfaces can create a more intuitive way for users to ask questions, receive information, and interact with AI models in real time.",
        "tools_used": "Python, LangChain, Google Gemini API, Streamlit, dotenv",
        "key_features": "Conversational AI chatbot interface.\nPrompt handling through LangChain agents.\nIntegration with Google Gemini models.\nPersistent chat history during a session.\nStreamlit-based browser interface for interaction.\nEnvironment variable management using dotenv.\nBeginner-friendly conversational workflow structure.",
        "role_contribution": "I built the chatbot workflow and connected LangChain with the Gemini API to process user prompts and generate responses. I worked through debugging model outputs, managing conversation history, and improving the user interaction flow while keeping the project simple and understandable.",
        "biggest_challenge": "One of the biggest challenges was understanding how LangChain structures messages and handles responses between the user, agent, and model. Debugging inconsistent outputs and managing chat history also required a lot of testing and iteration.",
        "lessons_learned": "This project helped me better understand how LLM applications are structured beyond simple API calls. I became more comfortable working with prompt flow, conversational memory, and debugging AI workflows while also learning how to present the interaction through a cleaner user interface.",
        "github_link": "https://github.com/benapple1/langchainAI.git",
        "demo_link": "",
        "category": "agent",
    },
    {
        "title": "Google AI Studio Media Project",
        "summary": "Used Google Flow and AI-generated assets to recreate and extend a cinematic scene through text-to-video generation workflows.",
        "business_problem": "Creating animated video content traditionally requires significant time, editing skill, and production resources. This project explored how generative AI tools can simplify and accelerate visual storytelling by turning text prompts and reference imagery into short cinematic video sequences.",
        "tools_used": "Google AI Studio, Google Flow, Nano Banana, Generative AI image tools, Prompt Engineering",
        "key_features": "AI-generated cinematic scene recreation.\nText-to-video animation workflow.\nCharacter and environment generation using prompts.\nScene extension and alternate ending generation.\nPrompt-driven visual consistency.\nShort-form AI video production pipeline.",
        "role_contribution": "I designed the prompts, generated the visual assets, and developed the scene workflow used to create the final video. This included describing characters, environments, style, and animation direction in enough detail to guide the model toward a consistent cinematic output.",
        "biggest_challenge": "One of the biggest challenges was maintaining visual consistency between frames while still generating natural movement and animation. It took multiple iterations and prompt refinements to balance creativity with continuity.",
        "lessons_learned": "This project helped me better understand how prompt specificity, scene description, and reference imagery impact AI-generated video quality. It also showed how generative AI tools can rapidly prototype visual ideas without traditional video production workflows.",
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
        "github_link": "https://github.com/benapple1/ml_appleby.git",
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
    "n8n Multi-Agent Handyman Workflow Project": "n8n Agent Workflow Project",
}


class Command(BaseCommand):
    help = "Seed the portfolio with the six required AI course projects."

    def handle(self, *args, **options):
        active_titles = {project["title"] for project in PROJECTS}
        alias_titles = set(PROJECT_TITLE_ALIASES.values())
        Project.objects.exclude(title__in=active_titles | alias_titles).delete()

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
