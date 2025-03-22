\version "2.24.3"
\language "english"
\header {
  title = ""
  composer = ""
  arranger = ""
  footnotes = ""
  copyright = "Creative Commons Attribution-ShareAlike 4.0"
}
\noPageBreak

info = {
    \key c \ionian
    \numericTimeSignature
    \time 4/4
    \tempo \markup {
      \italic Allegro
    } 4 = 100
}

main = \new StaffGroup <<
  % 🎻
  % 🎹
  % 🎸

  % 🥁
  \drums {
    \tempo 4 = 100
    \numericTimeSignature
    \time 4/4
 
    << 
      % 手上的音符
      {
        hh8 8 <<hh8 sn8>> hh8 8 8 <<hh8 sn8>> cymc8~
        cymc8 hh8 <<hh8 sn8>> hh8 8 8<<hh8 sn8>> hh8

        sn8 16 16 16 16 8
        hh8 hh8 <<hh8 sn8>> hh8 hh8 hh8 <<hh8 sn8>> hh8

        <<sn1 hh>>
        sn4^"L" 4^"R" 4_"L" 4_"R"
        16^"L" 16^"R" 8^"L" 8^"L" 16^"L" 16^"R"
        16_"L" 8_"R" 16_"R" r16 sn16_"R" 16_"L" 16_"R"

        sn8 8 8 8 \tuplet 3/2 4 {8 8 8 8 8 8}
        trio4 4 4 4
        trim4 4 4 4

        bd4 4 4 4
        bda4 4 4 4
        toml4 4 4 4 
        hh4 4 4 4
      } 
      % 脚上的音符
      \\ {
        bd4 r4 bd4 r4
      }

      % bd/bassdrum: 底鼓
      % sn/snare   : 军鼓
      % r          : 休止符
    >>
  }
>>

\book {
  \paper {

  }
}

\score {
  \main
  \layout {}
}

\score {
  \unfoldRepeats {
    \main
  }
  \midi {}
}

% REFS: https://lilypond.org/doc/Documentation/notation/percussion-notes
% REFS: https://pyonpyon.today/p/2021-07-write-drum-score-with-lilypond-on-arch
% REFS: https://www.imn.htwk-leipzig.de/~waldmann/etc/untutorial/lilypond/
