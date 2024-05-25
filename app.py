from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


app = Flask(__name__)

# Initialize the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/get_user_stories', methods=['POST'])
def get_user_stories():
    data = request.json
    user_id = data.get('userid')
    # print(user_id)
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    
    data_response = supabase.table('user_table').select('*').eq('id', user_id).single().execute()
    
    if not data_response:
        return jsonify({"error": "Database query failed"}), 500
    
    user, count = data_response  # Assuming the response is a tuple (user data, count)

    if count == 0:
        return jsonify({"error": "User not found"}), 404

    
    # story_ids = [user[1].get('storyId1'), user[1].get('storyId2'), user[1].get('storyId3')]
    story_ids = [user[1].get('storyId1')]
    print(story_ids)

    
    stories = []


    user_str = "User has watched the following contents:\n"
    for story_id in story_ids:
        if story_id is not None:
            print(type(story_id))
            story, count = supabase.table('success_story_table').select('*').eq('id', story_id).single().execute()
            
            user_str += "id: "+str(story[1].get('id'))+" "+story[1].get('type')+" about " + story[1].get('title_eng')+"\n"


            print(story)
            if story:
                stories.append(story)

    print(str)

    all_stories, count = supabase.table('success_story_table').select('*').execute()

    total_Str = "All available contents are:\n"
    for tstory in all_stories[1]:
        total_Str += "id: "+str(tstory.get('id'))+" "+tstory.get('type')+" about " + tstory.get('title_eng')+"\n"

    print(total_Str, user_str)

    prompt = f"""
    User has watched the following contents:
    {user_str}

    All available contents are:
    {total_Str}

    Recommend 4 ids from 'All available contents' that are not already watched by the user and are most relevant to what the user has watched. Order them based on relevance. The more relevent result should come first. Return only the ids as a list.
    For example:
    [10, 12, 2, 5]
    """

    recommended_ids_str = chat_gpt(prompt)
    print(recommended_ids_str)
    recommended_ids = recommended_ids_str.replace('[', '').replace(']', '').replace('\'', '').split(',')
    recommended_ids = [id.strip() for id in recommended_ids]
    
    recommendations = []
    for rec_id in recommended_ids:
        recommendation, count = supabase.table('success_story_table').select('*').eq('id', rec_id).single().execute()
        recommendations.append(recommendation[1])

    return jsonify(recommendations)

@app.route('/get_user_talks', methods=['POST'])
def get_user_talks():
    data = request.json
    user_id = data.get('userid')
    # print(user_id)
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    
    data_response = supabase.table('user_table').select('*').eq('id', user_id).single().execute()
    
    if not data_response:
        return jsonify({"error": "Database query failed"}), 500
    
    user, count = data_response  # Assuming the response is a tuple (user data, count)

    if count == 0:
        return jsonify({"error": "User not found"}), 404

    
    # talk_ids = [user[1].get('talkId1'), user[1].get('talkId2'), user[1].get('talkId3')]
    talk_ids = [user[1].get('talkId1')]
    # print(talk_ids)
    
    talks = []

    user_str = "User has watched the following contents:\n"
    for talk_id in talk_ids:
        if talk_id is not None:
            # print(type(talk_id))
            talk, count = supabase.table('expert_talks').select('*').eq('id', talk_id).single().execute()
            
            user_str += "id: "+str(talk[1].get('id'))+" "+talk[1].get('type')+" about " + talk[1].get('title_english')+"\n"


            # print(story)
            if talk:
                talks.append(talk)

    # print(str)

    all_talks, count = supabase.table('expert_talks').select('*').execute()

    total_Str = "All available contents are:\n"
    for ttalk in all_talks[1]:
        total_Str += "id: "+str(ttalk.get('id'))+" "+ttalk.get('type')+" about " + ttalk.get('title_english')+"\n"

    # print(total_Str, user_str)

    prompt = f"""
    User has watched the following contents:
    {user_str}

    All available contents are:
    {total_Str}

    Recommend 4 ids from 'All available contents' that are not already watched by the user and are most relevant to what the user has watched. Order them based on relevance. The more relevent result should come first. Return only the ids as a list.
    For example:
    [10, 12, 2, 5]
    """

    recommended_ids_str = chat_gpt(prompt)
    recommended_ids = recommended_ids_str.replace('[', '').replace(']', '').replace('\'', '').split(',')
    recommended_ids = [id.strip() for id in recommended_ids]
    
    recommendations = []
    for rec_id in recommended_ids:
        recommendation, count = supabase.table('expert_talks').select('*').eq('id', rec_id).single().execute()
        recommendations.append(recommendation[1])
        
    print(recommendation)
    return jsonify(recommendations)

# if __name__ == '__main__':
#     app.run(debug=True)