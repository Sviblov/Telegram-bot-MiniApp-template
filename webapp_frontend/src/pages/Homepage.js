import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import MiniApp  from './MiniApp';

function HomePage() {
  const navigate = useNavigate();

  useEffect(() => {
    const userIsValid = validateUser();

    if (!userIsValid) {
      navigate('/notTelegram');
    }
  }, [navigate]);

  return (
    <div>
      <MiniApp />
    </div>
  );
}

function validateUser() {


  // Replace with your actual validation logic
  return true; // For demonstration, always return false
}

export default HomePage;