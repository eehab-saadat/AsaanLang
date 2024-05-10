import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import PlayGround from "./pages/PlayGround";
import HomePage from "./pages/HomePage";
import Documentation from "./pages/Documentation";
import '@fortawesome/fontawesome-free/css/all.min.css';

export default function App() {
  return (
    <>
           

     <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />}/>
          <Route path="/PlayGround" element={<PlayGround />}/>
          <Route path="/Documentation" element={<Documentation />}/>
        </Routes>
    </BrowserRouter>
  

    </>
  );
}