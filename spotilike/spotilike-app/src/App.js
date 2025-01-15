import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Home from "./pages/home/homepage";
import Artiste from "./pages/artistes/artiste";
import AlbumDetail from "./pages/albums/albumDetail";
import AlbumsList from "./pages/albums/albumsList";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/albums" element={<AlbumsList />} />
          <Route path="/albums/:id" element={<AlbumDetail />} />
          <Route path="/artistes" element={<Artiste />} />

          {/* <Route path="/artistes/:id" element={<Artiste />} />
          <Route path="/albums/:id" element={<Artiste />} /> */}
          {/* Route pour les pages non trouvées */}
          {/* <Route path="*" element={<NotFound />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
