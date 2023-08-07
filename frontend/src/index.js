import React from 'react';
import ReactDOM from 'react-dom';
import { QueryClientProvider, QueryClient } from 'react-query'; // Import QueryClient and QueryClientProvider
import App from './App'; // Make sure the correct path is provided here
import './styles.css'; // Import your styles.css file

// Create a new QueryClient instance
const queryClient = new QueryClient();

ReactDOM.render(
  // Provide the QueryClient to the whole app using QueryClientProvider
  <QueryClientProvider client={queryClient}>
    <App />
  </QueryClientProvider>,
  document.getElementById('root')
);
