import openai
from PyPDF2 import PdfReader
import time
import os
import open_ai_api_key

def summarize_file(pdffilepath,destination_dir,s,e):
    total_word_count=0
    reader=PdfReader(pdffilepath)
    data=""
    openai.api_key=open_ai_api_key.api_key
    no_words=0
    chunk=""
    cnt=0
    print("This might take some time please wait")
    stime=time.time()
    filename="key-points_"+os.path.splitext(os.path.split(pdffilepath)[1])[0]+f"_({s}-{e}).txt"
    os.chdir(destination_dir)
    while(s<=e):
        page=reader.pages[s]
        text=page.extract_text()
        if(no_words+len(text)<=4000):
            total_word_count+=len(text)
            no_words+=len(text)
            chunk+=text
            cnt+=1
        else:
            try:
                completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",  messages=[{"role": "user", "content": f"Give key points for '{chunk}'"}] )
                summary=completion["choices"][0]["message"]["content"]
            except Exception as ex:
                time.sleep(21)
                s-=1
            else:
                with  open(filename,'a+',encoding='utf-8') as file:
                    file.write(f"Page {s-cnt} - {s-1}")
                    file.write("\n")
                    file.write(summary)
                    file.write("\n")
                print(f"Summarizing key points for pages {s-cnt} - {s-1}")
                data+=summary
                s-=1
                no_words=0
                chunk=""
                cnt=0
        s+=1
    if(data==""):
        completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",  messages=[{"role": "user", "content": f"Give key points for '{chunk}'"}] )
        data=completion["choices"][0]["message"]["content"]
        with  open(filename,'a+',encoding='utf-8') as file:
                file.write(f"Page {s-cnt} - {e}")
                file.write("\n")
                file.write(data)
                file.write("\n")
    print(f"Total word count: {total_word_count}\nKey Points:\n{data}")
    etime=time.time()
    return etime-stime


if __name__=="__main__":
    print("----SUMMARIZE PDF'S TO KEYPOINTS---")
    filepath=r'{}'.format(input("Enter path to pdf file: "))
    des_dir=r'{}'.format(input("Enter destination directory to save summary: "))
    start,end=map(int,input("Enter range (starting_page_number ending_page_number): ").split())
    timetake=summarize_file(filepath,des_dir,start,end)
    print(f"Time taken to summarize {end-start} pages: {timetake}sec\nKey points saved at {des_dir}")





