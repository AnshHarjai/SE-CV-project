from django.shortcuts import render

def cv_view(request):
    cv_data = {
        'name': 'Ansh Harjai',
        'title': 'MS Computer Science Student at NYU Tandon',
        'summary': "Graduate student specializing in Computer Science with hands-on experience in data science, software engineering, and AI. Strong background in building scalable systems, big data processing, and applied machine learning.",
        'skills': [
            'Python', 'C++', 'Java', 'Flask', 'REST APIs', 'HTML/CSS', 'JavaScript', 'Selenium',
            'MySQL', 'MongoDB', 'SQL Server', 'SQLAlchemy', 'Qdrant',
            'Git', 'Docker', 'Gradio', 'PowerBI', 'Tableau', 'PySpark',
            'PyTorch', 'TensorFlow', 'NLP', 'LangChain', 'LlamaIndex'
        ],
        'experience': [
            {
                'position': 'CSE Lab Assistant',
                'company': 'New York University',
                'years': 'Apr 2025 – Present',
                'details': [
                    "Manage and maintain 30 lab computers, ensuring smooth operation with regular OS updates and software installations.",
                    "Provide technical support to professors and students during lab sessions, improving session productivity.",
                    "Implemented regular maintenance checks, boosting lab efficiency and user satisfaction."
                ]
            },
            {
                'position': 'Data Science Intern',
                'company': 'Polestar Solutions',
                'years': 'Jan 2024 – May 2024',
                'details': [
                    "Deployed 3 AI-powered chatbots using Retrieval-Augmented Generation (RAG), improving query accuracy by 20%.",
                    "Optimized RESTful APIs with Flask, SQLAlchemy, and Azure AI Search, boosting response time by 30%.",
                    "Reduced SQL query times by 20% through database optimization and indexing.",
                    "Improved chatbot reliability by 25% via advanced prompt engineering using LangChain."
                ]
            },
            {
                'position': 'Software Engineering Intern',
                'company': 'HCLTech',
                'years': 'May 2023 – Jul 2023',
                'details': [
                    "Led a team of 4 to implement hybrid cloud solutions with AWS and Azure, cutting operational costs by 5% and improving security.",
                    "Designed PowerBI dashboards for enterprise datasets, enabling real-time analytics and faster decision-making."
                ]
            }
        ],
        'education': [
            {
                'degree': "Master of Science in Computer Science",
                'institution': "New York University, Tandon School of Engineering — Brooklyn, NY",
                'years': "Sep 2024 – May 2026",
                'gpa': "GPA 3.889/4.0",
                'coursework': [
                    "Design and Analysis of Algorithms I (A)",
                    "Big Data (A)",
                    "Information Visualization (A)",
                    "Artificial Intelligence (B+)"
                ]
            },
            {
                'degree': "Bachelor of Technology in Computer Science and Engineering",
                'institution': "Manipal University Jaipur — Rajasthan, India",
                'years': "Aug 2020 – May 2024",
                'awards': "Dean’s List (Semesters 6 and 7) | CGPA: 8.99/10"
            }
        ],
        'projects': [
            {
                'title': "Research-Net: Community Detections in Academic Papers",
                'timeline': "Jan 2025 – May 2025",
                'details': "Developed a Big Data pipeline using PySpark for distributed ETL, graph construction, and visualization to detect research communities.",
                'link': "https://github.com/AnshHarjai/Big-Data-Project-Research-Net"
            },
            {
                'title': "Retrieval-Augmented Generation (RAG) System",
                'timeline': "Sep 2024 – Dec 2024",
                'details': "Built a scalable LLM-powered RAG pipeline using Meta’s Llama-3-8B-Instruct, Docker, Gradio, MongoDB, and Qdrant for efficient contextual responses.",
                'link': "https://github.com/AnshHarjai/ai_project"
            },
            {
                'title': "Order and Donation Management System",
                'timeline': "Sep 2024 – Nov 2024",
                'details': "Designed a secure web platform using Flask and MySQL with SHA-256 encryption and RBAC, handling 500+ daily transactions.",
                'link': "https://github.com/AnshHarjai/WelcomeHome"
            },
            {
                'title': "Automated WhatsApp Broadcasting Tool",
                'timeline': "Aug 2023 – Dec 2023",
                'details': "Automated broadcasting of messages, images, and files to 100+ users using Python and Selenium, reducing manual effort by 50%.",
            }
        ],
        'contact': {
            'email': "ah7163@nyu.edu",
            'phone': "(646) 702-3732",
            'linkedin': "https://www.linkedin.com/in/ansh-harjai-7a422b245/",
            'github': "https://github.com/AnshHarjai",
            'location': "New York, NY"
        }
    }
    return render(request, 'cv.html', cv_data)