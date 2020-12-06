import requests
import slackweb
import time
from bs4 import BeautifulSoup



def main():
	urlName = "https://github.com/trending/python?since=daily"
	url = requests.get(urlName)
	soup = BeautifulSoup(url.content, "html.parser")
	py_groups = soup.find_all('article', class_='Box-row')
	
	for py_group in py_groups:
		tag_size = len(py_group)
		link_part = py_group.h1.a.get("href")
		title = link_part[1:]
		link_full = "https://github.com" + link_part
		attachments_all = []
		main_msg = {"title": title, "text": link_full}
		attachments_all.append(main_msg)
		slack = slackweb.Slack(url="")
		slack.notify(attachments=attachments_all)
		if tag_size == 9:
			abst = py_group.p.text.lstrip()
			attachments_abst = []
			abst_msg = {"text": abst}
			attachments_abst.append(abst_msg)
			slack.notify(attachments=attachments_abst)
		time.sleep(1)

	urlName = "https://github.com/trending/c++?since=daily"
	url = requests.get(urlName)
	soup = BeautifulSoup(url.content, "html.parser")
	cpp_groups = soup.find_all('article', class_='Box-row')

	for cpp_group in cpp_groups:
		tag_size = len(cpp_group)
		link_part = cpp_group.h1.a.get("href")
		title = link_part[1:]
		link_full = "https://github.com" + link_part
		attachments_all = []
		main_msg = {"title": title, "text": link_full}
		attachments_all.append(main_msg)
		slack = slackweb.Slack(url="")
		slack.notify(attachments=attachments_all)
		if tag_size == 9:
			abst = cpp_group.p.text.lstrip()
			attachments_abst = []
			abst_msg = {"text": abst}
			attachments_abst.append(abst_msg)
			slack.notify(attachments=attachments_abst)
		time.sleep(1)


if __name__ == '__main__':
	main()