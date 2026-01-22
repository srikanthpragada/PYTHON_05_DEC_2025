data = """
Copilot is an AI-powered digital assistant from Microsoft that acts as a "copilot" to help with various tasks, from answering questions and generating content to summarizing information and automating workflows. It is integrated into many Microsoft products, including Windows, Microsoft 365 apps like Word and Excel, and can be accessed through web browsers and mobile apps. The assistant uses advanced AI to provide creative and informative help, streamline work, and boost productivity. 
How it works AI-powered assistant: Copilot uses advanced AI to understand your requests and provide responses, content, and creative assistance.
Contextual understanding: It can provide assistance that is relevant to the specific Microsoft 365 app you are using, such as drafting emails in Outlook or analyzing data in Excel.
Internet-connected: Copilot can search the web to provide you with up-to-date information and summaries of subjects.
Work and personal use: It can assist with a wide range of tasks, from complex work-related activities like drafting reports and analyzing data to personal needs like planning travel or learning new skills. 
"""

import re

words = re.findall(r'\w+', data.upper())

for w in sorted(set(words)):
  print(f"{w:15}  {words.count(w)}")


