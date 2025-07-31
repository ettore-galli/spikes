\version "2.22.2"

\header {
  title = "Send in the Clowns (Tin Whistle in D)"
  composer = "Stephen Sondheim"
}

melody = \relative d' {
  \key d \major
  \time 4/4
  \tempo "Rubato, espressivo"
  
  % Introduzione (prima frase)
  r4 b'8( a) g4 fis8( e) |
  d4 e fis g |
  a4.( b8) a4 g8( fis) |
  e2. r4 |
  
  % "Isn't it rich..."
  b'4 a8( g) fis4 e8( d) |
  e4 fis g a |
  b4.( cis8) b4 a8( g) |
  fis2. r4 |
  
  % "Don't you love farce?"
  d'4 b a b |
  g4.( a8) g4 fis8( e) |
  d4 e fis g |
  a2. r4 |
  
  % "Me, I've fallen..."
  b4 a g fis |
  e4.( fis8) e4 d8( cis) |
  d4 e fis g |
  a2. r4 \bar "|."
}

\score {
  \new Staff {
    \clef treble
    \melody
  }
  \layout { }
  \midi { tempoWholesPerMinute = #60 }
}