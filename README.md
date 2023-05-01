# Summarize-PDF-to-Keypoints-with-ChatGPT
PDF Summarization with ChatGPT-3.5! This repository contains a Python script that uses the power of ChatGPT, a large language model trained by OpenAI, to summarize PDF documents into key points.
<br><br>Open API key has restriction on number of token generated per prompt which ranges from 2048 tokens to 4096 tokens per prompt. 
This means that the length of the prompt text string must not exceed the specified token limit, including any additional parameters or options that are included in the API request.<br>
Our script can summarize text well over the lenght of 4096 tokens by dividing text into sizeable amount of chunks and summarizing the chunks.<br>But this comes at the cost of time take to summarize.

To summarize a 45 page pdf containg over 88,000 words it take around 562 second which is 9 min 36 sec.<br>
![img1](https://user-images.githubusercontent.com/110279690/235439280-ab5fbb51-1f80-425b-94f3-50c0bb30d513.jpg)<br><br>
![img3](https://user-images.githubusercontent.com/110279690/235439305-5532950d-7ca4-4859-92ac-f63e717ec9e3.jpg)<br><br>
![img4](https://user-images.githubusercontent.com/110279690/235439398-e522c69d-9e65-454e-bca3-499abe99a9d9.jpg)

