import React, { useState, useEffect } from 'react';
import Modal from './Modal';
import { useQuery } from 'react-query';

const QuoteList = () => {
  const [quotes, setQuotes] = useState([]);
  const [selectedQuote, setSelectedQuote] = useState(null);
  const [quotesToShow, setQuotesToShow] = useState(5);
  const quotesPerPage = 5;
  const [errorMessage, setErrorMessage] = useState(null);

  useEffect(() => {
    fetch('http://0.0.0.0:8000/api/v1/get-quotes')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch quotes');
        }
        return response.json();
      })
      .then((data) => setQuotes(data))
      .catch((error) => {
        console.error('Error fetching data:', error);
        setErrorMessage('Failed to fetch quotes. Please try again later.');
      });

    const handleScroll = () => {
      const { scrollTop, clientHeight, scrollHeight } = document.documentElement;
      if (scrollTop + clientHeight >= scrollHeight - window.innerHeight) {
        setQuotesToShow((prev) => Math.min(prev + quotesPerPage, quotes.length));
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, [quotes.length, quotesPerPage]);

  const fetchAuthorInfo = async (authorName) => {
    try {
      const response = await fetch(`http://0.0.0.0:8000/api/v1/get-author-info?author_name=${authorName}`);
      if (!response.ok) {
        throw new Error('Failed to fetch author info');
      }
      const data = await response.json();
      return {
        date_of_birth: data.date_of_birth,
        bio: data.bio,
        books: data.books.map((book) => book),
      };
    } catch (error) {
      console.error(error);
      setErrorMessage('Failed to fetch author info. Please try again later.');
      throw new Error('Failed to fetch author info');
    }
  };

  const { data: authorInfo, isLoading } = useQuery(
    ['authorInfo', selectedQuote?.author.name],
    () => fetchAuthorInfo(selectedQuote?.author.name),
    {
      enabled: !!selectedQuote?.author.name,
    }
  );

  const openModal = async (quote) => {
    try {
      setSelectedQuote(quote);
    } catch (error) {
      console.error(error);
    }
  };

  const closeModal = () => {
    setSelectedQuote(null);
  };

  return (
    <div>
      <h1 className="center-text">Quotes</h1>
      {errorMessage && <p className="error-message">{errorMessage}</p>}
      {quotes.slice(0, quotesToShow).map((quote, index) => (
        <div key={index} className="quote-container">
          {/* Quote details */}
        </div>
      ))}
      <Modal isOpen={selectedQuote !== null} onRequestClose={() => setSelectedQuote(null)} />
    </div>
  );
};

export default QuoteList;
