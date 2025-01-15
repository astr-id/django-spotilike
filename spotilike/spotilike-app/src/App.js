import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Sidebar from "./components/Sidebar";
import Footer from "./components/Footer";
import Home from "./pages/home/homepage";
import Albums from "./pages/albums/albums";
import Artiste from "./pages/artistes/artiste";
import ArtisteDetails from "./pages/artistes/ArtisteDetails";

function App() {
  return (
    <Router>
      <div className="flex h-screen bg-black text-white">
        <Sidebar />

        <div className="flex-1 overflow-auto p-4">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/albums" element={<Albums />} />
            <Route path="/artistes" element={<Artiste />} />
            <Route path="/artistes/:id" element={<ArtisteDetails />} />
          </Routes>
        </div>
      </div>
      <Footer />
    </Router>
  );
}

export default App;
