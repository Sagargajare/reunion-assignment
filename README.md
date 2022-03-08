# Backend Assignment - REUNION

### Problem Statement

Build APIs for a social media platform in either NodeJS or Python. The API should support features like getting a user profile, follow a user, upload a post, delete a post, like a post, unlike a liked post, and comment on a post. Design the database schema and implement in PostgreSQL.

**Using Token**
```
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "demouser@sagargajare.in", "password": "demouser"}' \
  http://localhost:8000/api/authenticate
```

```javascript
{'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ2NjcwOTIzLCJpYXQiOjE2NDY2NzA2MjMsImp0aSI6IjAzYzEzMGE2YmQ5ODQwN2M4MzUxNWQ5YjRlODIxNzlmIiwidXNlcl9pZCI6MX0._o2SrwPg8eXnR9ZQ77V6shx05LQOL2ShOrjg20kUKfw',
 'refresh_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0Njc1NzAyMywiaWF0IjoxNjQ2NjcwNjIzLCJqdGkiOiIwN2IxODFmNjdiMGY0ZjBlODhhMWE2NjRlMjBhMDgyNSIsInVzZXJfaWQiOjF9.vBRC48Zb-IiXXHEREiVI-9e8DS5ZT-gAH19S2uCZ0q4',
 'user': {'email': 'demouser@sagargajare.in',
          'followers': 0,
          'following': 0,
          'pk': 1,
          'username': 'demouser'}}
```

Pass Header as: Authorization: Bearer <access_token>

Generating Access Token

<br>
**API Endpoints**

- POST /api/authenticate should perform user authentication and return a JWT token.
    - INPUT: Email, Password
    - RETURN: JWT token
    
    <aside>
    ➡️ **NOTE:** Use dummy email & password for authentication. No need to create endpoint for registering new user.
    
    </aside>
    
- POST /api/follow authenticated user would follow user with {id}
```javascript
{
    "follower_id": user_id,
}
```


user_id: id of the user to be followed

- DELETE /api/follow/{id} authenticated user would unfollow a user with {id}
- GET /api/user should authenticate the request and return the respective user profile.
    - RETURN: User Name, number of followers & followings.
- POST api/posts/ would add a new post created by the authenticated user.
    - Input: Title, Description
    - RETURN: Post-ID, Title, Description, Created Time(UTC).
- DELETE api/posts/{id} would delete post with {id} created by the authenticated user.
- POST /api/like/{id} would like the post with {id} by the authenticated user.
```javascript
{
    "post_id": post_id,
}
```
post_id: id of the post to be liked
- DELETE /api/like/{id} would unlike the post with {id} by the authenticated user.
- POST /api/comment/{id} add comment for post with {id} by the authenticated user.
    - Input: Comment
    - Return: Comment-ID
```javascript
{
    "post_id": post_id,
    "input": input
}
```
post_id: id of the post to be commented
input: comment to be added

- GET api/posts/{id} would return a single post with {id} populated with its number of likes and comments
- GET /api/all_posts would return all posts created by authenticated user sorted by post time.
    - RETURN: For each post return the following values
        - id: ID of the post
        - title: Title of the post
        - desc: Description of the post
        - created_at: Date and time when the post was created
        - comments: Array of comments, for the particular post
        - likes: Number of likes for the particular post

### **Stacks**

- Backend: NodeJS (using ExpressJS or Koa) or Python (using Django). Use other helping libraries.
- Database: PostgreSQL or MongoDB

### Submission Details

- Implement the mentioned functionalities by writing your code & hosting it on Heroku
- Submit the Heroku hosted link for the deployed APIs and Github or Gitlab public repository link for the deployed code in the form below