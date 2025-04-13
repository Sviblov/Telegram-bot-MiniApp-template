
import WebAppValidator from './components/WebAppValidator.tsx';
import 'antd/dist/reset.css';
import ErrorBoundary from './components/ErrorBoundary.tsx';


const App = () => {
 
  return (
    <ErrorBoundary>
    
        <WebAppValidator />

    </ErrorBoundary>
  );
};

export default App
