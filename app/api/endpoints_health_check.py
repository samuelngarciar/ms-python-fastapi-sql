from fastapi import APIRouter, Depends
from flask import jsonify

router = APIRouter()

@router.get("/health")
 def health_check():
    return jsonify({"status": "ok"}), 200
