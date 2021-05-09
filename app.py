# coding=utf-8

# inspired by https://dev.to/xarala221/python-rest-apis-with-fastapi-crud-application-9kc
#   ... FastAPI\ -\ A\ python\ framework\ _\ Full\ Course-7t2alSnE2-I
#   ... https://testdriven.io/blog/fastapi-crud/
#   ... https://fastapi.tiangolo.com/async/
#   ... https://github.com/pluralsight/tech-blog-fastapi-demo
#   ... https://github.com/mjhea0/awesome-fastapi
#   ... https://www.toptal.com/python/build-high-performing-apps-with-the-python-fastapi-framework
#   ... https://phrase.com/blog/posts/fastapi-i18n/

# app.py
from fastapi import FastAPI, status, Response, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime


app = FastAPI()
postdb = [
{
  "idno": 11,
  "title": "Getting started with FastAPI",
  "author": "George",
  "content": "Hello FastAPI",
  "created_at": "2021-05-05T10:10:10.1010Z",
  "published_at": "2021-05-05T11:11:11.1111Z",
  "published": True
},
{
  "idno": 22,
  "title": "Getting started with FastAPI",
  "author": "George",
  "content": "Added async, tags, test, url params, Dockerfile, readme, fixed delete, TODO auth, router, frontend GUI",
  "created_at": "2021-05-09T10:10:10.1010Z",
  "published_at": "2021-05-09T11:11:11.1111Z",
  "published": True
}
]


# post model
class Post(BaseModel):
    idno: int
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False


@app.get("/", tags=['Test'])
async def read_root():
    """just return something for the root path"""
    return {"home": "easy blog management Rest API in Python using Fast API"}


@app.get("/ping", tags=['Test'])
async def pong():
    return {"ping": "pong!"}


@app.get("/blog", tags=['Blog'])
async def list_blog_posts(limit:int=10, startfrom:int=0):
    """List blog posts: ?limit=10&startfrom=0"""
    return postdb[startfrom:startfrom+limit]


@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['No auth yet'])
async def create_new_post(post: Post):
    """Creating a new blog post - CREATE"""
    postdb.append(post.dict())
    return postdb[-1]


@app.get("/blog/{post_id}", status_code = status.HTTP_200_OK, tags=['Blog'])
async def view_post_detail(post_id: int, response: Response):
    """View blog post detail - READ - zero based index in blog list"""
    if post_id >= len(postdb):
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"error: post_id {post_id} out of range, postdb length is {len(postdb)}"}
    else:
        return postdb[post_id]


@app.put("/blog/{post_id}", status_code = status.HTTP_202_ACCEPTED, tags=['No auth yet'])
async def edit_post(post_id: int, post: Post):
    """Editing blog post - UPDATE - zero based index in blog list"""
    postdb[post_id] = post
    return {"message": "Post has been updated succesfully"}


@app.delete("/blog/{post_id}", status_code = status.HTTP_204_NO_CONTENT, tags=['No auth yet'])
async def delete_post(post_id: int):
    """Deleting blog post - DELETE - zero based index in blog list"""
    postdb.pop(post_id)
    return {"message": "Post has been deleted succesfully"}

