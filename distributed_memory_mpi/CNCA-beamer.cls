\ProvidesClass{CNCA-beamer} 
\ProcessOptions\LoadClass[aspectratio=169,mathserif,t]{beamer}

\RequirePackage[english]{babel}
\RequirePackage[utf8]{inputenc}

%Figuras
\RequirePackage{graphicx, subfigure}
\RequirePackage[]{tikz}
\RequirePackage{pbox}

%Matemática
\RequirePackage{amsmath}
\RequirePackage{amssymb}

%Algoritmos
\RequirePackage{float}
\RequirePackage{algorithm}
\RequirePackage{algorithmicx}
\RequirePackage{algpseudocode}
\RequirePackage{listings}


\RequirePackage{color}
\RequirePackage{hyperref}

\RequirePackage{mdframed}
\RequirePackage{tcolorbox}
\RequirePackage{multicol}


\RequirePackage{caption}
\RequirePackage{decorule}




\usetheme{Frankfurt}
\setbeamertemplate{navigation symbols}{}

\definecolor{darkblue}{rgb}{0 , 0.054 , 0.196}
\setbeamercolor{title}{fg=white, bg=darkblue}
\setbeamercolor{frametitle}{fg=white, bg=darkblue}
\setbeamercolor{box}{fg=white, bg=darkblue}

\usecolortheme{whale}

\lstset{language=Python,
  numbers=left,
  inputencoding=latin1,
  basicstyle=\footnotesize\ttfamily,
  keywordstyle=\color{blue},         
  breaklines=true, 
  showtabs=false,
  showstringspaces=false,
  numberstyle=\tiny\color{darkblue}
}  


\beamersetuncovermixins{\opaqueness<1>{10}}{\opaqueness<2->{15}}
\setbeamertemplate{bibliography item}{}


\AtBeginSection[]{
  \begin{frame}
  \vfill
  \centering
  \begin{beamercolorbox}[sep=8pt,center,shadow=true,rounded=true]{title}
    \usebeamerfont{title}\insertsectionhead\par%
  \end{beamercolorbox}
  \vfill
  \end{frame}
}


\def\institution#1		{\gdef\@institution{#1}}
\def\department#1		{\gdef\@department{#1}}
\def\subdepartment#1		{\gdef\@subdepartment{#1}}

\def\subject#1		{\gdef\@subject{#1}}
\def\code#1		{\gdef\@code{#1}}
\def\title#1		{\gdef\@title{#1}}
\def\subtitle#1	{\gdef\@subtitle{#1}}

\def\degree#1		{\gdef\@degree{#1}}
\def\author#1		{\gdef\@author{#1}}
\def\email#1		{\gdef\@email{#1}}

\def\date#1		{\gdef\@date{#1}}
\def\place#1		{\gdef\@place{#1}}

\newcommand{\BLANKSPACE}{\color{white}{.}}


%%%%%%%%%%% title page

\newcommand{\titlePage}
{
    \begin{frame}[plain]
    \begin{center}
        \begin{tikzpicture}[overlay, remember picture]
            \node[anchor=north west, %anchor is upper left corner of the graphic
                xshift=1cm, %shifting around
                yshift=-1cm] 
                at (current page.north west) %left upper corner of the page
            {\includegraphics[height=1.25cm]{img/logoL.png}}; 
        \end{tikzpicture}
        \begin{tikzpicture}[overlay, remember picture]
            \node[anchor=north east, %anchor is upper left corner of the graphic
                xshift=-1cm, %shifting around
                yshift=-1cm] 
                at (current page.north east) %left upper corner of the page
            {\includegraphics[height=1.25cm]{img/logoR.png}}; 
        \end{tikzpicture}
    
        {\Large \@institution}\\
        {\large \@department}\\
        {\large \@subdepartment}\\ 

        {\large \textbf{\texttt{\@code} \@subject}}
        
        \vspace{0.25in}
        
        \begin{beamercolorbox}[rounded=true, center, shadow=true]{box}
            {

            
                \vspace{4mm}
                {\LARGE \@title}\\
                {\@subtitle}\\ 
                \vspace{5mm}
            }
        \end{beamercolorbox}
        
        % \vspace{0.1in}
        \begin{center}
            % \@degree ~ 
            \@author\\
            \url{\@email}
        \end{center}
        
        % \vspace{0.1in}
    
        {\small 
            \@date\\
            \@place
        }
    \end{center}
    \end{frame}

}