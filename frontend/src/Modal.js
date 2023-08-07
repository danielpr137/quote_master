import React from 'react';

const Modal = ({ isOpen, onRequestClose, authorInfo, isLoading }) => {
  return (
    <div>
      {isOpen && (
        <div className="Modal">
          <button className="close-button" onClick={onRequestClose}>
            X
          </button>
          <div className="modal-header">
            <h2>Author Info:</h2>
          </div>
          {isLoading ? (
            <p>Loading...</p>
          ) : (
            <div>
              <p>Date of Birth: {authorInfo?.date_of_birth}</p>
              <p>Bio: {authorInfo?.bio}</p>
              <p>Books:</p>
              <ul>
                {authorInfo?.books.map((bookTitle, index) => (
                  <li key={index}>{bookTitle}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default Modal;
