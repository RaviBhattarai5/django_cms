import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import OrderPage from './components/OrderPage.jsx'; // New component for orders
import PlacementPage from './components/PlacementPage.jsx'; // New component for orders

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/orders" element={<OrderPage />} />
                <Route path="/placements" element={<PlacementPage />} />
            </Routes>
        </Router>
    );
}

export default App;