import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { BsLinkedin, BsGithub } from 'react-icons/bs';
import CircularProgress from '@mui/material/CircularProgress';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import './App.css';

const App: React.FC = () => {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [countdown, setCountdown] = useState(20);
  const [error, setError] = useState<string | null>(null);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = async () => {
    setLoading(true);
    setResponse(null);
    setCountdown(20);
    setError(null); // Reset error state
    try {
      const res = await axios.post('https://caixa-431702.rj.r.appspot.com/ask_question', { question });
      setResponse(res.data.answer);
    } catch (error) {
      setError('Erro ao obter resposta. Tente novamente.');
    } finally {
      setLoading(false); // Ensure loading is set to false
    }
  };

  useEffect(() => {
    let timer: NodeJS.Timeout;
    if (loading && countdown > 0) {
      timer = setInterval(() => {
        setCountdown((prevCountdown) => prevCountdown - 1);
      }, 1000); // Alterado para 1000 milissegundos
    } else if (countdown === 0) {
      setLoading(false);
    }

    return () => clearInterval(timer);
  }, [loading, countdown]);

  return (
    <html lang="en">
      <head>
        <link
          rel="stylesheet"
          href="https://unpkg.com/tailwindcss@2.2.19/dist/tailwind.min.css"
        />
        <link
          href="https://unpkg.com/@tailwindcss/custom-forms/dist/custom-forms.min.css"
          rel="stylesheet"
        />
        <style>
          {`@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap");
          html {
            font-family: "Poppins", -apple-system,
              BlinkMacSystemFont, "Segoe UI", Roboto,
              "Helvetica Neue", Arial, "Noto Sans",
              sans-serif, "Apple Color Emoji",
              "Segoe UI Emoji", "Segoe UI Symbol",
              "Noto Color Emoji";
          }`}
        </style>
      </head>

      <body className="leading-normal tracking-normal text-gray-100 m-6 bg-cover bg-fixed">
        <div className="h-full">
          <div className="w-full container mx-auto">
            <div className="w-full flex items-center justify-between">
              <a
                className="flex items-center text-white no-underline hover:no-underline font-bold text-2xl lg:text-4xl"
                href="#"
              >
                Assistente
                <span className="bg-clip-text text-transparent bg-gradient-to-r text-yellow-700 ">
                  CEF
                </span>
              </a>
              <div className="flex w-1/2 justify-end content-center">
                <a
                  className="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-right h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out"
                >
                  Acesse as redes sociais
                </a>
                <a
                  className="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-right h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out"
                  href="https://github.com/victoresende19"
                  target="_blank"
                >
                  <BsGithub />
                </a>
                <a
                  className="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-right h-10 p-2 md:h-auto md:p-4 transform hover:scale-125 duration-300 ease-in-out"
                  href="https://www.linkedin.com/in/victor-resende-508b75196/"
                  target="_blank"
                >
                  <BsLinkedin />
                </a>
              </div>
            </div>
          </div>

          <div className="container pt-24 md:pt-36 mx-auto flex flex-wrap flex-col md:flex-row items-center">
            <div className="flex flex-col w-full xl:w-2/5 justify-center lg:items-start">
              <p className="leading-normal text-base md:text-2xl mb-8 text-justify md:text-left text-white">
                O assistente CEF tem como objetivo responder a perguntas específicas sobre o código de ética e conduta para funcionários e servidores da Caixa Econômica Federal, com base no documento disponível no site <a className="inline-block text-blue-300 no-underline hover:text-pink-500 hover:text-underline text-right transform hover:scale-100 duration-300 ease-in-out" href="https://www.caixa.gov.br/Downloads/caixa-asset/Codigo-de-Etica-e-de-Conduta.pdf" target="_blank">Caixa Asset</a>.
              </p>
              <form className="bg-gray-900 opacity-75 w-full shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4">
                <div className="mb-4">
                  <label className="block text-yellow-600 py-2 font-bold mb-2" htmlFor="movieInput">
                    Pergunte algo relacionado à ética e conduta da Caixa!
                  </label>
                  <div className="relative">
                    <TextField
                      id="outlined-multiline-flexible"
                      value={question}
                      onChange={handleInputChange}
                      multiline
                      rows={3}
                      placeholder="Faça uma pergunta..."
                      className="shadow appearance-none border rounded w-full py-2 px-3 text-black bg-white leading-tight focus:outline-none focus:shadow-outline"
                    />
                  </div>
                </div>
                <div className="flex items-center pt-4">
                  {loading ? (
                    <>
                      <div className="text-white">Isso pode levar cerca de {countdown} segundos...</div>
                    </>
                  ) : (
                    <button
                      className="bg-gradient-to-r from-yellow-500 to-yellow-900 text-slate-50 font-bold py-2 px-4 rounded focus:ring transform transition hover:scale-105 duration-300 ease-in-out"
                      type="button"
                      onClick={handleSubmit}
                      disabled={loading}
                    >
                      Perguntar
                    </button>
                  )}
                </div>
              </form>
            </div>

            <div className="w-full xl:w-3/5 p-12 overflow-hidden relative flex justify-center items-center">
              {loading ? (
                <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '200px' }}>
                  <CircularProgress color="inherit" />
                </Box>
              ) : (
                <>
                  {error ? (
                    <div className="bg-gray-900 opacity-75 w-full text-center shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4">
                      <span className="bg-clip-text bg-gradient-to-r from-white to-orange-500">
                        {error}
                      </span>
                    </div>
                  ) : (
                    <>
                      {response ? (
                        <div className="bg-gray-900 opacity-75 w-full text-center shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4">
                          <p className="my-4 text-3xl md:text-5xl text-white font-bold leading-tight">
                            <span className="bg-clip-text bg-gradient-to-r from-white to-orange-500">
                              Resposta
                            </span>
                          </p>
                          <p className="text-white text-xl text-left">
                            {response}
                          </p>
                        </div>
                      ) : (
                        <div className="bg-gray-900 opacity-75 w-full text-center shadow-lg rounded-lg px-8 pt-6 pb-8 mb-4">
                          <span className="bg-clip-text text-transparent font-bold  bg-gradient-to-r from-yellow-600 to-yellow-700 text-3xl">
                            Sua resposta aparecerá aqui
                          </span>
                        </div>
                      )}
                    </>
                  )}
                </>
              )}
            </div>
            <div className="w-full pt-16 pb-6 text-sm text-center md:text-left fade-in">
              <a className="text-gray-500 no-underline hover:no-underline" href="#">&copy; 2024 </a>
              - Victor Augusto Souza Resende
            </div>
          </div>
        </div>
      </body>
    </html>
  );
};

export default App;
