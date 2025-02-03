import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";
import AlbumsList from "./pages/albums/albumsList";
import Artiste from "./pages/artistes/artiste";
import AlbumDetail from "./pages/albums/albumDetail";
import ArtisteDetails from "./pages/artistes/ArtisteDetails";
import Home from "./pages/home/homepage";
import Header from "./components/header";

function App() {
  return (
    <Router>
      <div className="text-white min-h-screen">
        <Header />
        <div className="flex min-h-screen">
          <Sidebar />
          <div className="w-full min-h-screen overflow-hidden m-3">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/albums" element={<AlbumsList />} />
              <Route path="/albums/:id" element={<AlbumDetail />} />
              <Route path="/artistes" element={<Artiste />} />
              <Route path="/artistes/:id" element={<ArtisteDetails />} />
            </Routes>
          </div>
        </div>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
