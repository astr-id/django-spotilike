import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Albums from "./pages/albums/albums";
import Home from "./pages/home/homepage";
import Artiste from "./pages/artistes/artiste";

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/albums" element={<Albums />} />
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
