import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});

export const fetchArticles = async () => {
  const response = await API.get("articles/");
  return response.data;
};
