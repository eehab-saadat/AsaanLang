import React, { useState } from 'react';
import AceEditor from 'react-ace';
import 'ace-builds/src-noconflict/mode-python';
import 'ace-builds/src-noconflict/theme-monokai';
import NavBar from '../components/NavBar';

const CodeEditor = ({ onCodeChange }) => {
  const handleEditorChange = (newValue) => {
    onCodeChange(newValue);
  };

  return (
    <>
      <AceEditor
        mode="python"
        theme="monokai"
        onChange={handleEditorChange}
        fontSize={14}
        showPrintMargin={true}
        showGutter={true}
        highlightActiveLine={true}
        setOptions={{
          enableBasicAutocompletion: true,
          enableLiveAutocompletion: true,
          enableSnippets: false,
          showLineNumbers: true,
          tabSize: 2,
        }}
        className='code-editor'
        
      />
    </>
  );
};

const PlayGround = () => {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');

  const handleCodeChange = (newCode) => {
    setCode(newCode);
  };

  const handleRunButtonClick = async () => {
    fetch('http://127.0.0.1:5000/input_source', {
      method: 'POST',
      headers: {
        // Set the Content-Type header correctly
        'Content-Type': 'application/json',
      },
      mode: 'cors',
      body: JSON.stringify({source_code: code}), // Use the FormData object
    });

    const response = await fetch('http://127.0.0.1:5000/output');
    const data = await response.json();
    setOutput(data.target_code);
    
  };
  
  return (
    <>
        <NavBar />
      <div className='playground'>
        <div className='playground-headings'>
           <h1>Input</h1>
           <h1>Output</h1>
          </div>
        <div className='playground-container'>
          <CodeEditor onCodeChange={handleCodeChange} className='code-editor' />
          <textarea className='output' value={output} readOnly />
        </div>

        <div className='btn'>
          <button className="run-btn" onClick={handleRunButtonClick}>
            Chalao
          </button>
        </div>
      </div>
    </>
  );
};

export default PlayGround;
