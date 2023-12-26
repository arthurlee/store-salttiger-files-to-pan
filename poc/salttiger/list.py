from bs4 import BeautifulSoup
import requests
import re
from record import Record

html = '''
<ul class="car-list">
	<li><span class="car-yearmonth">2023年12月 <span title="文章数量">(30)</span></span>
		<ul class='car-monthlisting'>
			<li>21: <a href="https://salttiger.com/training-data-for-machine-learning/">Training Data for Machine Learning</a> <span title="评论数量">(0)</span></li>
			<li>19: <a href="https://salttiger.com/locksport-a-hackers-guide-to-lockpicking-impressioning-and-safe-cracking/">Locksport: A Hacker’s Guide to Lockpicking, Impressioning, and Safe Cracking</a> <span title="评论数量">(4)</span></li>
			<li>19: <a href="https://salttiger.com/postgresql-16-administration-cookbook/">PostgreSQL 16 Administration Cookbook</a> <span title="评论数量">(0)</span></li>
			<li>19: <a href="https://salttiger.com/mastering-tableau-2023-4th-edition/">Mastering Tableau 2023, 4th Edition</a> <span title="评论数量">(0)</span></li>
			<li>19: <a href="https://salttiger.com/modern-data-architecture-on-aws/">Modern Data Architecture on AWS</a> <span title="评论数量">(0)</span></li>
			<li>19: <a href="https://salttiger.com/unity-cookbook-5th-edition/">Unity Cookbook, 5th Edition</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/learning-digital-identity/">Learning Digital Identity</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/managing-cloud-native-data-on-kubernetes/">Managing Cloud Native Data on Kubernetes</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/learning-microsoft-azure/">Learning Microsoft Azure</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/building-serverless-applications-on-knative/">Building Serverless Applications on Knative</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/alteryx-designer-the-definitive-guide/">Alteryx Designer: The Definitive Guide</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/build-your-own-database-from-scratch/">Build Your Own Database From Scratch</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/build-your-own-redis-with-c-cpp/">Build Your Own Redis with C/C++</a> <span title="评论数量">(0)</span></li>
			<li>18: <a href="https://salttiger.com/from-source-code-to-machine-code-build-your-own-compiler-from-scratch/">From Source Code To Machine Code: Build Your Own Compiler From Scratch</a> <span title="评论数量">(0)</span></li>
			<li>05: <a href="https://salttiger.com/learn-ai-assisted-python-programming-with-github-copilot-and-chatgpt/">Learn AI-Assisted Python Programming: With GitHub Copilot and ChatGPT</a> <span title="评论数量">(0)</span></li>
			<li>05: <a href="https://salttiger.com/grokking-concurrency/">Grokking Concurrency</a> <span title="评论数量">(0)</span></li>
			<li>05: <a href="https://salttiger.com/essential-typescript-5-3rd-edition/">Essential TypeScript 5, 3rd Edition</a> <span title="评论数量">(0)</span></li>
			<li>05: <a href="https://salttiger.com/distributed-machine-learning-patterns/">Distributed Machine Learning Patterns</a> <span title="评论数量">(0)</span></li>
			<li>05: <a href="https://salttiger.com/pro-aspdotnet-core-7-10th-edition/">Pro ASP.NET Core 7, 10th Edition</a> <span title="评论数量">(0)</span></li>
			<li>05: <a href="https://salttiger.com/aspdotnet-core-in-action-3rd-edition/">ASP.NET Core in Action, 3rd Edition</a> <span title="评论数量">(0)</span></li>
			<li>04: <a href="https://salttiger.com/hacker-culture-a-to-z/">Hacker Culture A to Z</a> <span title="评论数量">(0)</span></li>
			<li>04: <a href="https://salttiger.com/data-science-the-hard-parts/">Data Science: The Hard Parts</a> <span title="评论数量">(0)</span></li>
			<li>04: <a href="https://salttiger.com/machine-learning-with-r-4th-edition/">Machine Learning with R, 4th Edition</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/generative-ai-on-aws/">Generative AI on AWS</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/kubernetes-cookbook-2nd-edition/">Kubernetes Cookbook, 2nd Edition</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/cloud-native-development-with-google-cloud/">Cloud Native Development with Google Cloud</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/mastering-bitcoin-3rd-edition/">Mastering Bitcoin, 3rd Edition</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/applied-embedded-electronics/">Applied Embedded Electronics</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/digitalization-of-financial-services-in-the-age-of-cloud/">Digitalization of Financial Services in the Age of Cloud</a> <span title="评论数量">(0)</span></li>
			<li>01: <a href="https://salttiger.com/csharp-12-in-a-nutshell/">C# 12 in a Nutshell</a> <span title="评论数量">(0)</span></li>
		</ul>
	</li>
 	<li><span class="car-yearmonth">2023年11月 <span title="文章数量">(14)</span></span>
		<ul class='car-monthlisting'>
			<li>21: <a href="https://salttiger.com/cloud-observability-in-action/">Cloud Observability in Action</a> <span title="评论数量">(0)</span></li>
			<li>21: <a href="https://salttiger.com/csharp-12-and-dotnet-8-modern-cross-platform-development-fundamentals-8th-edition/">C# 12 and .NET 8: Modern Cross-Platform Development Fundamentals, 8th Edition</a> <span title="评论数量">(0)</span></li>
			<li>21: <a href="https://salttiger.com/fastapi/">FastAPI</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/a-pythonic-adventure/">A Pythonic Adventure</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/program-management-for-open-source-projects/">Program Management for Open Source Projects</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/algorithmic-thinking-2nd-edition/">Algorithmic Thinking, 2nd Edition</a> <span title="评论数量">(1)</span></li>
			<li>15: <a href="https://salttiger.com/the-art-of-machine-learning/">The Art of Machine Learning</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/ios-17-app-development-essentials/">iOS 17 App Development Essentials</a> <span title="评论数量">(1)</span></li>
			<li>15: <a href="https://salttiger.com/ios-17-programming-for-beginners-8th-edition/">iOS 17 Programming for Beginners, 8th Edition</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/windows-11-for-enterprise-administrators-2nd-edition/">Windows 11 for Enterprise Administrators, 2nd Edition</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/learn-postgresql-2nd-edition/">Learn PostgreSQL, 2nd Edition</a> <span title="评论数量">(0)</span></li>
			<li>15: <a href="https://salttiger.com/full-stack-development-with-spring-boot-3-and-react-4th-edition/">Full Stack Development with Spring Boot 3 and React, 4th Edition</a> <span title="评论数量">(0)</span></li>
			<li>14: <a href="https://salttiger.com/head-first-python-3rd-edition/">Head First Python, 3rd Edition</a> <span title="评论数量">(0)</span></li>
			<li>14: <a href="https://salttiger.com/csharp-12-pocket-reference/">C# 12 Pocket Reference</a> <span title="评论数量">(0)</span></li>
		</ul>
	</li>
 </ul>
 '''
 
def extract_group(li_month):
    month_text = li_month.select_one('.car-yearmonth').text
    print(month_text)
    m = re.search("(\d+)年(\d+)月 \((\d+)\)", month_text)   #\u5e74(\d+)\u6708
    group = Record()
    group.year = m.group(1)
    group.month = m.group(2)
    group.book_count = m.group(3)
    return group

    
def extract_books(li_month):
    books = []
    li_book_list = li_month.select('.car-monthlisting > li')
    for li_book in li_book_list:
        link_a = li_book.select_one('a')
        book = Record()
        
        book.day = li_book.contents[0].replace(': ', '')
        book.name = link_a.text
        book.detail_url = link_a['href']
        # print(book)
        books.append(book)
        
    return books
    

web_data = requests.get('https://salttiger.com/archives/')
soup = BeautifulSoup(web_data.content, 'html.parser')
# soup = BeautifulSoup(html, 'html.parser')
li_month_list = soup.select('.car-list > li')

group_list = []

for li_month in li_month_list:
    group = extract_group(li_month)
    # print(group.year, group.month, group.book_count)
    books = extract_books(li_month)
    group.books = books
    
    group_list.append(group)
    
    
print(group_list)