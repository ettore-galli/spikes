\version "2.22.2"

\header {
  title = "10 Esercizi per Flauto Dolce Sopranino in Fa"
  composer = "Esercizi elementari"
}

\paper {
  indent = 0\mm
  line-width = 120\mm
}

\layout {
  \context {
    \Score
    \override SpacingSpanner.common-shortest-duration = #(ly:make-moment 1/8)
  }
}

sopranino = {
  \key f \major
  \time 4/4
  \tempo "Moderato"
  \set Staff.instrumentName = "Sopranino in Fa"
  \set Staff.midiInstrument = "recorder"
  
  % Esercizio 1 - Scala di Fa maggiore
  \relative c'' {
    \mark "1. Scala di Fa maggiore"
    c4 d e f | g a bes c | bes a g f | e d c2 \bar "||"
  }
  
  % Esercizio 2 - Intervalli di terza
  \relative c'' {
    \mark "2. Intervalli di terza"
    c4 e d f | e g f a | g bes a g | f e d c \bar "||"
  }
  
  % Esercizio 3 - Salti semplici
  \relative c'' {
    \mark "3. Salti semplici"
    c4 g' d a' | e bes' f c' | g d' a e' | bes f' c2 \bar "||"
  }
  
  % Esercizio 4 - Ritmi elementari
  \relative c'' {
    \mark "4. Ritmi elementari"
    c8 d e f g4 g | a8 bes a g f4 f | g8 a g f e4 e | f8 g f e d c4. \bar "||"
  }
  
  % Esercizio 5 - Arpeggio di Fa
  \relative c'' {
    \mark "5. Arpeggio di Fa"
    c4 e g c | g e c e | g c e g | c2 c, \bar "||"
  }
  
  % Esercizio 6 - Esercizio di articolazione
  \relative c'' {
    \mark "6. Articolazione"
    c8-.\staccato d-. e-. f-. g-. a-. bes-. c-. | bes-.\staccato a-. g-. f-. e-. d-. c4\tenuto \bar "||"
  }
  
  % Esercizio 7 - Pattern ritmico
  \relative c'' {
    \mark "7. Pattern ritmico"
    c4. d8 e4 f | g8 a bes4 c bes | a g f e | d c2. \bar "||"
  }
  
  % Esercizio 8 - Cambi di dinamica
  \relative c'' {
    \mark "8. Dinamiche"
    c4\p d e\cresc f | g a bes c\f | bes\> a g f\! | e d c2 \bar "||"
  }
  
  % Esercizio 9 - Esercizio cromatico
  \relative c'' {
    \mark "9. Cromatismo"
    c4 cis d e | f fis g a | bes b c cis | d c bes a \bar "||"
  }
  
  % Esercizio 10 - Melodia semplice
  \relative c'' {
    \mark "10. Melodia"
    c4 d e f | g2 a4 bes | c bes a g | f e d c \bar "|."
  }
}

\score {
  \new Staff \with {
    \clef treble
    instrumentName = "Sopranino"
  } \sopranino
  \layout { }
  \midi { \tempo 4 = 100 }
}