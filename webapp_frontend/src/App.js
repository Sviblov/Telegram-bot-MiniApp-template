import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/Homepage';
import NotTelegram from './pages/nottelegram';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/nottelegram" element={<NotTelegram />} />
      </Routes>
    </Router>
  );
}

export default App;