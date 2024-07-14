import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import MiniApp from './MiniApp';

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
  const debug = process.env.REACT_APP_DEBUG === 'true'

  if (debug) {
   
    return true; // For demonstration, always return false
  } else {
    return false;
  }
}

export default HomePage;