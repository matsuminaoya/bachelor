from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

#Dictionary of article text data
article_dict = {
"article_1":"""text_data_article_1""",
"article_2":"""text_data_article_2""",
"article_3":"""text_data_article_3""",
"article_4":"""text_data_article_4""",
"article_5":"""text_data_article_5""",
"article_6":"""text_data_article_6""",
"article_7":"""text_data_article_7""",
"article_8":"""text_data_article_8""",
"article_9":"""text_data_article_9""",
"article_10":"""text_data_article_10"""
}
#Run the following program in each article
for article in article_dict.values():

    #Initialize chat
    chat = ChatOpenAI(model_name="gpt-3.5-turbo-1106", 
                    temperature=0,
                    openai_api_key="your_api_key")

    #Initialize memory
    memory = ConversationBufferMemory()

    #Initialize chain
    conversation = ConversationChain(
        llm=chat,
        memory=memory
    )

    #Conversation 1
    input_1 = "Can you extract the proper nouns from the text I give next?"
    res = conversation.run(input_1)
    #Command and response outputs
    print("Input 1: "+input_1)
    print(res)

    #Conversation 2
    #input_2 = "The article text data"
    res = conversation.run(article)
    #Command and response outputs
    print("Input 2: "+"The article text data")
    print(res)

    #Conversation 3 to 14
    #Dictionary of Commands
    input_dict = {
    "input_3":"""Can you restrict the previous result to those belonging to "Organization"?""",
    "input_4":"""Can you restrict the previous result to those belonging to "Person"?""",
    "input_5":"""Can you restrict the previous result to those belonging to "Location"?""",
    "input_6":"""Can you restrict the previous result to those belonging to "Commodity"?""",
    "input_7":"""Can you describe the relationships that apply "Person WorksFor Organization"?""",
    "input_8":"""Can you describe the relationships that apply "Organization CompetesWith Organization"?""",
    "input_9":"""Can you describe the relationships that apply "Organization CollaborateWith Organization"?""",
    "input_10":"""Can you describe the relationships that apply "Person CollaborateWith Person"?""",
    "input_11":"""Can you describe the relationships that apply "Organization IsPartOf Organization"?""",
    "input_12":"""Can you describe the relationships that apply "Organization OperatesIn Location"?""",
    "input_13":"""Can you describe the relationships that apply "Organization Produces Commodity"?""",
    "input_14":"""Can you describe the relationships that apply "Organization Consumes Commodity"?"""
    }
    #Run each command
    n = 3
    for input in input_dict.values():
        res = conversation.run(input)
        #Command and response outputs
        print("Input "+str(n)+": "+input)
        print(res)
        n += 1

    #Conversation 15
    input_15 = """Can you describe all the relationships in Turtle format triples. Please output in the format starting from "@prefix ex:"?"""
    #Command and response outputs
    res = conversation.run(input_15)
    print("Input 15: "+input_15)
    print(res)