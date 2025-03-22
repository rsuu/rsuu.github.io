import {
  animate,
  spring,
} from "https://cdn.jsdelivr.net/npm/motion@latest/+esm";

// REFS: https://motion.dev/docs/animate
animate(
  ".anim-box",
  { rotate: 360 },
  {
    // duration: 10,
    repeat: Infinity,
    // ease: "linear",
    type: spring,
    stiffness: 300,
  },
);
