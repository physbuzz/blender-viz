Just a repo to keep track of my work with Blender



# Blender Scientific Visualization Learning Path

## 1. Quick Cornell Box Viz

TODO:
- [x] Basic cornell box setup w/ Cornell
- [x] Render via CLI
- [x] Render via Python script

![](p1-cornellbox/p1_0001.png)

Misc. notes:
- Workspaces at the top of the screen are different collections of editors. The icon+dropdown at the top left of each panel are the editor types.
- Usual keyboard operations: s for scale, g for translate, r for rotate. shift+a to add object (make sure you choose right; object mode vs editor mode).
- 1, 2, 3 to switch between vertex / face select while in edit mode.
- HDRs can be added in Properties Editor -> World -> Surface -> Color. 
- Output directory is in prop editor -> output prop -> output
- Version of blender installed through apt wouldn't work with Cycles, but extracting the tar.gz from blender did work. 

## 2. Animate the Cornell box + rotating object

TODO:
- [ ] Create a parented hierarchy (?) of objects
- [ ] Create an animation of the rotating objects
- [ ] CLI render and combine into a .gif

## 3. Create a "planets size comparison" render
- [ ] Get planet textures
- [ ] Create size comparison animation

- Learn camera path animation basics
- Understand how to overlay things like text onto videos
- Understand terminology like timeline, dope sheet, f-curves, animation nodes

## 4. Import + render some mathematical objects from Mathematica

## 5. Physics and Blender's Simulation Tools
- [ ] Water simulation: Dam break + transparent materials 
- [ ] Caltrops + funnel simulation

notes: 
- If possible, tie in some aspect of node based materials (Pool tiles?)
- "Learn basic simulation caching for complex scenes" (?)

## 6. Programming: Sound visualizer
- Project that used geometry nodes
- Project using Python

## 7. Programming: complex logistic map

## 8. Programming: double pendulum
