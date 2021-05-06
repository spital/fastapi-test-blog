# coding=utf-8

# inspired by https://dev.to/xarala221/python-rest-apis-with-fastapi-crud-application-9kc

# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime


app = FastAPI()
postdb = []


# post model
class Post(BaseModel):
    id: int
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: datetime
    published: Optional[bool] = False


@app.get("/")
def read_root():
  return {"home": "easy blog management Rest API in Python using Fast API"}


@app.get("/blog")
def list_blog_posts():
    """List blog posts"""
    return postdb


@app.post("/blog")
def create_new_post(post: Post):
    """Creating a new blog post - CREATE"""
    postdb.append(post.dict())
    return postdb[-1]


@app.get("/blog/{post_id}")
def view_post_detail(post_id: int):
    """View blog post detail - READ"""
    post = post_id - 1
    return postdb[post]


@app.post("/blog/{post_id}")
def edit_post(post_id: int, post: Post):
    """Editing blog post - UPDATE"""
    postdb[post_id] = post
    return {"message": "Post has been updated succesfully"}


@app.delete("/blog/{post_id}")
def delete_post(post_id: int):
    """Deleting blog post - DELETE"""
    postdb.pop(post_id-1)
    return {"message": "Post has been deleted succesfully"}
