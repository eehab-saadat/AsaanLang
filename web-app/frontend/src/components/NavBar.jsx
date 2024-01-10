import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Outlet } from 'react-router-dom';

export default function NavBar() {
  const location = useLocation();

  return (
    <>
      <div className="navbar">
        <div className="logo">
          <h1 className="primary-color">
            <Link to="/" >
              Asaan
            </Link>
          </h1>
          <h1>Lang</h1>
        </div>

        <div className="navbar-pages">
          <Link to="/Documentation" className={`page-nav ${location.pathname === '/Documentation' ? 'underline' : ''}`}>
            Dastawezaat
          </Link>
          <Link to="/PlayGround" className={`page-nav ${location.pathname === '/PlayGround' ? 'underline' : ''}`}>
            Code Medaan
          </Link>
        </div>
        <i className="fa-brands fa-github fa-2xl"></i>
      </div>
      <Outlet />
    </>
  );
}
