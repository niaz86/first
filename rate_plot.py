{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>New Start</h1>\n",
    "# import library\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Export the current environment's packages to a requirements.txt file\n",
    "#!pip freeze > requirements.txt\n",
    "#!apt-get install git  # For systems where apt-get is available\n",
    "# Stage and commit changes\n",
    "#!git add requirements.txt\n",
    "#!git commit -m \"Add or update requirements.txt\"\n",
    "\n",
    "# Push changes to GitHub\n",
    "#!git push origin master  # Replace 'main' with the correct branch name\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import datetime\n",
    "import pandas as pd\n",
    "from lxml import html\n",
    "import os\n",
    "\n",
    "url = \"https://www.bajus.org/gold-price\"\n",
    "\n",
    "headers = {\n",
    "    \"Accept\": \"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\",\n",
    "    \"Accept-Language\": \"en-US,en;q=0.9,bn;q=0.8\",\n",
    "    \"Cache-Control\": \"max-age=0\",\n",
    "    \"Connection\": \"keep-alive\",\n",
    "    \"Cookie\": \"XSRF-TOKEN=eyJpdiI6InlNYlM0aXlTOW1oSC9rbUtaWktpZUE9PSIsInZhbHVlIjoieWtsUGFGQ01BNDFuT0t2cG13YXY1WUlvZ3V6empFRWhISkZkVXpDK0tuUDFmVm1tQ3A1Y3oySTJEbEQ1ZFJ2ZFdCbEg4QlBWK0tsT1gyTWtiNCthaklCNnVJZzk3YlgwUExob1NDQU5zdVhlb2hxbUJtTEN3eHJTTEgxTnhmYUEiLCJtYWMiOiI5ZjNmOGY4ZDgyZGJiNDY4MDQ2ZjlhM2E5N2ViNGE0Y2IwYTk2NjkzZDMwNzAwYmVmNzMyNTI1N2QxNTI5MjZhIiwidGFnIjoiIn0%3D; bajus_session=eyJpdiI6IlRuMzJlcVlaZlVyZ2htOTBEL29idWc9PSIsInZhbHVlIjoiQjlpK202bVpUbE1BWHQ1MUFReHlxQmg1TjBON0tGa3hhSzBUVW5xckM2Sk90UkJLNDVuSitpTkgxT1JMWTBrQ2dWb0xhcGNVampKeFM5cHNRclozeGo3MWViVmI3UzQxMXNFMVk0Y0pjL0E5Uzk1UGYxRzNMWlRseUN1Z0VZWXUiLCJtYWMiOiI3OTZmNDY2YTdlN2YwMmMwOTY4YTUxYzhmMWE0ZDc3NTY1MzEzYmMzOGVjNjRjZTYxMDdmNmU2ZWQzOWM1YzU2IiwidGFnIjoiIn0%3D\",\n",
    "    \"Referer\": \"https://www.google.com/\",\n",
    "    \"Sec-Fetch-Dest\": \"document\",\n",
    "    \"Sec-Fetch-Mode\": \"navigate\",\n",
    "    \"Sec-Fetch-Site\": \"cross-site\",\n",
    "    \"Sec-Fetch-User\": \"?1\",\n",
    "    \"Upgrade-Insecure-Requests\": \"1\",\n",
    "    \"User-Agent\": \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36\",\n",
    "    \"sec-ch-ua\": '\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"',\n",
    "    \"sec-ch-ua-mobile\": \"?0\",\n",
    "    \"sec-ch-ua-platform\": '\"Windows\"'\n",
    "}\n",
    "\n",
    "# Send GET request with the headers\n",
    "response = requests.get(url, headers=headers)\n",
    "\n",
    "# Check the status code\n",
    "print(response.status_code)\n",
    "\n",
    "tree=html.fromstring(response.content)\n",
    "\n",
    "Time=datetime.datetime.now().strftime('%#I:%#M:%S %p')\n",
    "Gold_pro_name=[]\n",
    "Silver_pro_name=[]\n",
    "for i in tree.xpath('/html/body/section/div/div//table/tbody/tr/th/h6/text()'):\n",
    "    names=i.strip()\n",
    "    if 'Gold' in names:\n",
    "        Gold_pro_name.append(names)\n",
    "    else:\n",
    "        Silver_pro_name.append(names)\n",
    "\n",
    "prices=tree.xpath('/html/body/section/div//div/table/tbody/tr/td/span/text()')\n",
    "\n",
    "Gold_price=[]\n",
    "for i in prices[0:4]:\n",
    "    k=int(i.split(' ')[0].replace(',',''))\n",
    "    Gold_price.append(k)\n",
    "Silver_price=[]\n",
    "for i in prices[4:]:\n",
    "    k=int(i.split(' ')[0].replace(',',''))\n",
    "    Silver_price.append(k) \n",
    "\n",
    "file_path='Analysis of Silver marketing.csv'    \n",
    "if Silver_price!=None:\n",
    "    z={}\n",
    "    for x,y in zip(Silver_pro_name,Silver_price):\n",
    "        z[x]=[y]      \n",
    "    data=pd.DataFrame(z,index=[Time]) \n",
    "    if os.path.exists(file_path):\n",
    "        data.to_csv(file_path,mode='a',header=False)\n",
    "    else:\n",
    "        data.to_csv(file_path)\n",
    "file_path='Analysis of Gold marketing.csv'\n",
    "if Gold_price!=None:\n",
    "    z={}\n",
    "    for x,y in zip(Gold_pro_name,Gold_price):\n",
    "        z[x]=[y]      \n",
    "    data=pd.DataFrame(z,index=[Time]) \n",
    "    if os.path.exists(file_path):\n",
    "        data.to_csv(file_path,mode='a',header=False)\n",
    "    else:\n",
    "        data.to_csv(file_path)\n",
    "  "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}