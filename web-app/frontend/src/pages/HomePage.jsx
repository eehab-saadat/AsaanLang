import React from 'react';
import {useState, useEffect} from 'react';
import NavBar from '../components/NavBar';
import {Link } from 'react-router-dom';



const LoadingScreen = () => (
    <div className="loading-screen">
        <h1 id="loading-screen-logo" className="pulsing-element"><span className="primary-color">Asaan</span><span className="black">Lang</span></h1>
      <h1>AB CODING HUI ASAAN...</h1>
    </div>
  );


export default function HomePage() {
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
      const runLoadingScreen = () => {
        setTimeout(() => {
          setIsLoading(false);
        }, 3000); 
      };
  
      runLoadingScreen(); 

      return () => {
      };
    }, []);
  

  return (
    <>
     {isLoading ? (
        <LoadingScreen />
      ) :
    <div>
      <NavBar />
      <>
        <div className = 'homepage'>
            <div className='hero-section'>
                <img src='./src/assets/hero-section-img.png' alt='hero-section-img' className='hero-section-img' />
                <div className = 'asaanlang-description'>
                    <h1><strong><span className='primary-color'>Asaan</span>Lang</strong></h1>
                    <h4>AsaanLang<strong> Urdu/Hindi <b>Par</b> Mabni Aik Transpiled Coding Ki Zubaan Hai Jo Nihayat Sada, Samajhne Mein Asaan Aur Tez-raftaar Hai</strong></h4>
                </div>
            </div>
            <div className='homepage-section-1'>
                <img src='./src/assets/code-snippet.jpeg' alt='code-snippet' className='homepage-section-1-img' />
                <div className='homepage-section-1-section'>
                    <h2 className='white'><b>Ab Urdu-Hindi Ki Apnaaiyat Ke Saath Programming Ki Dunya Me Apna Pehla Kadam Rakhein </b></h2>
                    <div className='homepage-section-1-btns'>
                        <button className='homepage-section-1-btn'><Link to='/PlayGround' className='homepage-btn-link'><b>Code  Krein</b></Link></button>
                        <button className='homepage-section-1-btn'><Link to='/Documentation' className='homepage-btn-link'><b>Khud Seekhein</b></Link></button>
                    </div>
                </div>
            </div>
            <div className='homepage-section-2'>
                <div className ='card'>
                    <img src='./src/assets/building-blocks.png' alt='building-blocks' className='homepage-section-2-img' />
                    <h2><b>Asaan</b></h2>
                    <h4>Saaf aur<br></br>sada Syntax</h4>
                </div>
                <div className ='card'>
                    <img src='./src/assets/lightning.png' alt='lightning' className='homepage-section-2-img' />
                    <h2><b>Barq Raftaar</b></h2>
                    <h4>Bijli se tez aur<br></br> istemaal me halki</h4>
                </div>
                <div className ='card'>
                    <img src='./src/assets/coffee.png' alt='coffee'/>
                    <h2><b>Bila-Takalluf</b></h2>
                    <h4>Seekhne aur<br></br> istemaal me asaan</h4>
                </div>
            </div>
            <footer className='footer'>
                <div className='footer-container'>
                    <div className='footer-description'>
                        <h2 className='white'>AsaanLang ke saath coding <br></br> seekho, apni zubaan me!</h2>
                    </div>
                    <div className='footer-icons'>
                        <i className="fa-brands fa-instagram fa-2xl -icon"></i>
                        <i className="fa-brands fa-facebook fa-2xl -icon"></i>
                        <i className="fa-brands fa-reddit fa-2xl -icon"></i>
                    </div>
                </div>
                <p className='white'><sm>AsaanLang@gmail.com</sm></p>
            </footer>
               
        </div>
      </>
    </div>}
    </>
  );
}