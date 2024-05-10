import React from "react";
import {useEffect, useState} from "react";
import NavBar from "../components/NavBar";

export default function Documentation(){
    const [activeHeading, setActiveHeading] = useState("");

    useEffect(() => {
      const handleScroll = () => {
        const scrollPosition = window.scrollY;
  
        const headings = [
          "installation",
          "intro",
          "contents",
          "data-types",
          "variables",
          "loops",
        ];
  
        for (const heading of headings) {
          const element = document.getElementById(heading);
          if (element && element.offsetTop <= scrollPosition + 60) {
            setActiveHeading(heading);
          }
        }
      };
  
      window.addEventListener("scroll", handleScroll);
  
      return () => {
        window.removeEventListener("scroll", handleScroll);
      };
    }, []);
  
    return(
        <>  
            <NavBar />
            <div className='documentation-page' >
                <div className='documentation-navbar' activeSection={activeHeading}>
                    <h2><strong><a>Khush Amadeed</a></strong></h2>
                    <div className='doc-navbar-contents'><strong><a href="#installation" className={activeHeading === "installation" ? "active" : ""}>Installation</a></strong></div>
                    <div className='doc-navbar-contents'><strong><a href="#intro" className={activeHeading === "intro" ? "active" : ""}>Taruf(Intro)</a></strong></div>
                    <div className='doc-navbar-contents'><strong><a href="#contents" className={activeHeading === "contents" ? "active" : ""}>Fehrist(Contents)</a></strong></div>
                    <div className='doc-navbar-contents'><strong><a href="#data-types" className={activeHeading === "data-types" ? "active" : ""}>Data Types</a></strong></div>
                    <div className='doc-navbar-contents'><strong><a href="#variables" className={activeHeading === "variables" ? "active" : ""}>Variables</a></strong></div>
                    <div className='doc-navbar-contents'><strong><a href="#loops" className={activeHeading === "loops" ? "active" : ""}>Loops</a></strong></div>
                </div>
                <div className='documentation-container' id="documentation-container">
                    <h1 className='primary-color' id="khush-amadeed">AsaanLang Shuru karein</h1>
                    <h2>AsaanLang ke sath ab coding kelie angrezi ki zarorat nahi. Urdu-Hindi ki saadagi aur apnaaiyat se faida uthate hue be-fikr ho ke coding krein aur apni zindagi asaan krein.</h2>
                    <div className='filler' id="installation"></div>
                    <h2 className='primary-color' id="installation">Installation</h2>
                    <h3>AsaanLang ko apni muqaami device par install knre aur chalane ke liye niche diye gaye steps per amal karein:" </h3>
                    <ol>
                        <li>GitHub repository ko apni muqaami device per “download” krein. Agar aapke paas Git he tu aap yeh command bhi istemaal kr sakte hein:
                        </li>
                        <div className='clone-code-block' id="code-block">
                            git clone https://github.com/eehab-saadat/AsaanLang
                        </div>
                        <li>
                        AsaanLang ko muqaami device per istemaal krne kelie Python aur NodeJS pehle se install hona zaoori he. Agar aapke paas dono cheezein installed nahi hein tu diye gaye links per click krke unke download page per ja kr install krein.
                        </li>
                        <li>
                        Jis folder me aap ne AsaanLang install ki he, wahan ja kr terminal kholein aur neche di gayi commands ko chalaein:
                        </li>
                        <div className='clone-code-block'>
                            python setup.py
                        </div>
                    </ol>
                    <div>
                        <h4>Mubarak ho! Aap ne kamiyaabi se AsaanLang download krli he. Ab AsaanLang transpiler ki tamaam khubion se faida uthane kelie help menu kholein aur transpiler ko chalana seekhein:</h4>
                    </div>
                    <div className='clone-code-block'>
                        python transpile.py -h
                    </div>
                    <h2 className='primary-color'><br></br>Chalane Ke Tareekey</h2>
                    <div>
                        <div className='clone-code-block'>
                        (Web App Kelie:) python transpile.py -w <br></br>
                        (Command Line Kelie:) python transpile.py

                    </div>
                            
                       
                    </div>
                    <div className='filler' id="intro"></div>
                    <h2 className='primary-color' >Taruf(Intro)</h2>
                    <h3>AsaanLang ko apni muqaami device par install knre aur chalane ke liye niche diye gaye steps per amal karein:" </h3>
                    <ol>
                        <li>GitHub repository ko apni muqaami device per “download” krein. Agar aapke paas Git he tu aap yeh command bhi istemaal kr sakte hein:
                        </li>
                        <div className='clone-code-block' id="code-block">
                            git clone https://github.com/eehab-saadat/AsaanLang
                        </div>
                        <li>
                        AsaanLang ko muqaami device per istemaal krne kelie Python aur NodeJS pehle se install hona zaoori he. Agar aapke paas dono cheezein installed nahi hein tu diye gaye links per click krke unke download page per ja kr install krein.
                        </li>
                        <li>
                        Jis folder me aap ne AsaanLang install ki he, wahan ja kr terminal kholein aur neche di gayi commands ko chalaein:
                        </li>
                        <div className='clone-code-block'>
                            npm install --save-dev
                            <br></br>
                            pip install -r requirements.txt
                        </div>
                    </ol>
                    <div>
                        <h4>Mubarak ho! Aap ne kamiyaabi se AsaanLang download krli he. Ab AsaanLang chalane kelie neche di gayi command ko terminal per chalaein aur AsaanLang sei lutf andoz huiye:</h4>
                    </div>
                    <div className='clone-code-block'>
                        npm start-backend
                        <br></br>
                        npm run start
                    </div>
                    <div className='filler' id="contents"></div>
                    <h2 className='primary-color' >Fehrist(Contents)</h2>
                    <h3>AsaanLang ko apni muqaami device par install knre aur chalane ke liye niche diye gaye steps per amal karein:" </h3>
                    <ol>
                        <li>GitHub repository ko apni muqaami device per “download” krein. Agar aapke paas Git he tu aap yeh command bhi istemaal kr sakte hein:
                        </li>
                        <div className='clone-code-block' id="code-block">
                            git clone https://github.com/eehab-saadat/AsaanLang
                        </div>
                        <li>
                        AsaanLang ko muqaami device per istemaal krne kelie Python aur NodeJS pehle se install hona zaoori he. Agar aapke paas dono cheezein installed nahi hein tu diye gaye links per click krke unke download page per ja kr install krein.
                        </li>
                        <li>
                        Jis folder me aap ne AsaanLang install ki he, wahan ja kr terminal kholein aur neche di gayi commands ko chalaein:
                        </li>
                        <div className='clone-code-block'>
                            npm install --save-dev
                            <br></br>
                            pip install -r requirements.txt
                        </div>
                    </ol>
                    <div>
                        <h4>Mubarak ho! Aap ne kamiyaabi se AsaanLang download krli he. Ab AsaanLang chalane kelie neche di gayi command ko terminal per chalaein aur AsaanLang sei lutf andoz huiye:</h4>
                    </div>
                    <div className='clone-code-block'>
                        npm start-backend
                        <br></br>
                        npm run start
                    </div>
                    <div className='filler' id="data-types"></div>
                    <h2 className='primary-color' >Data Types</h2>
                    <h3>AsaanLang ko apni muqaami device par install knre aur chalane ke liye niche diye gaye steps per amal karein:" </h3>
                    <ol>
                        <li>GitHub repository ko apni muqaami device per “download” krein. Agar aapke paas Git he tu aap yeh command bhi istemaal kr sakte hein:
                        </li>
                        <div className='clone-code-block' id="code-block">
                            git clone https://github.com/eehab-saadat/AsaanLang
                        </div>
                        <li>
                        AsaanLang ko muqaami device per istemaal krne kelie Python aur NodeJS pehle se install hona zaoori he. Agar aapke paas dono cheezein installed nahi hein tu diye gaye links per click krke unke download page per ja kr install krein.
                        </li>
                        <li>
                        Jis folder me aap ne AsaanLang install ki he, wahan ja kr terminal kholein aur neche di gayi commands ko chalaein:
                        </li>
                        <div className='clone-code-block'>
                            npm install --save-dev
                            <br></br>
                            pip install -r requirements.txt
                        </div>
                    </ol>
                    <div>
                        <h4>Mubarak ho! Aap ne kamiyaabi se AsaanLang download krli he. Ab AsaanLang chalane kelie neche di gayi command ko terminal per chalaein aur AsaanLang sei lutf andoz huiye:</h4>
                    </div>
                    <div className='clone-code-block'>
                        npm start-backend
                        <br></br>
                        npm run start
                    </div>
                    <div className='filler' id="variables"></div>
                    <h2 className='primary-color' >Variables</h2>
                    <h3>AsaanLang ko apni muqaami device par install knre aur chalane ke liye niche diye gaye steps per amal karein:" </h3>
                    <ol>
                        <li>GitHub repository ko apni muqaami device per “download” krein. Agar aapke paas Git he tu aap yeh command bhi istemaal kr sakte hein:
                        </li>
                        <div className='clone-code-block' id="code-block">
                            git clone https://github.com/eehab-saadat/AsaanLang
                        </div>
                        <li>
                        AsaanLang ko muqaami device per istemaal krne kelie Python aur NodeJS pehle se install hona zaoori he. Agar aapke paas dono cheezein installed nahi hein tu diye gaye links per click krke unke download page per ja kr install krein.
                        </li>
                        <li>
                        Jis folder me aap ne AsaanLang install ki he, wahan ja kr terminal kholein aur neche di gayi commands ko chalaein:
                        </li>
                        <div className='clone-code-block'>
                            npm install --save-dev
                            <br></br>
                            pip install -r requirements.txt
                        </div>
                    </ol>
                    <div>
                        <h4>Mubarak ho! Aap ne kamiyaabi se AsaanLang download krli he. Ab AsaanLang chalane kelie neche di gayi command ko terminal per chalaein aur AsaanLang sei lutf andoz huiye:</h4>
                    </div>
                    <div className='clone-code-block'>
                        npm start-backend
                        <br></br>
                        npm run start
                    </div>
                    <div className='filler' id="loops"></div>
                    <h2 className='primary-color' >Loops</h2>
                    <h3 >AsaanLang ko apni muqaami device par install knre aur chalane ke liye niche diye gaye steps per amal karein:" </h3>
                    <ol>
                        <li>GitHub repository ko apni muqaami device per “download” krein. Agar aapke paas Git he tu aap yeh command bhi istemaal kr sakte hein:
                        </li>
                        <div className='clone-code-block' id="code-block">
                            git clone https://github.com/eehab-saadat/AsaanLang
                        </div>
                        <li>
                        AsaanLang ko muqaami device per istemaal krne kelie Python aur NodeJS pehle se install hona zaoori he. Agar aapke paas dono cheezein installed nahi hein tu diye gaye links per click krke unke download page per ja kr install krein.
                        </li>
                        <li>
                        Jis folder me aap ne AsaanLang install ki he, wahan ja kr terminal kholein aur neche di gayi commands ko chalaein:
                        </li>
                        <div className='clone-code-block'>
                            npm install --save-dev
                            <br></br>
                            pip install -r requirements.txt
                        </div>
                    </ol>
                    <div>
                        <h4>Mubarak ho! Aap ne kamiyaabi se AsaanLang download krli he. Ab AsaanLang chalane kelie neche di gayi command ko terminal per chalaein aur AsaanLang sei lutf andoz huiye:</h4>
                    </div>
                    <div className='clone-code-block'>
                        npm start-backend
                        <br></br>
                        npm run start
                    </div>
                </div>
            </div>
        </>
    )
}