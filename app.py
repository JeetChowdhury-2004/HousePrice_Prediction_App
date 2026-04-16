components.html("""
<!DOCTYPE html>
<html>
<head>

<!-- Bootstrap -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Three.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128/examples/js/controls/OrbitControls.js"></script>

<!-- Typed.js -->
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>

<style>
body {
    margin:0;
    background:#0f172a;
    color:white;
    font-family: 'Segoe UI', sans-serif;
}

#canvas-container {
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 10px 30px rgba(0,0,0,0.4);
}

.header-text {
    text-align:center;
    padding:10px;
    font-size:22px;
    font-weight:bold;
}
</style>

</head>

<body>

<div class="container mt-2">

    <!-- Typed Text -->
    <div class="header-text">
        <span id="typed"></span>
    </div>

    <!-- 3D Canvas -->
    <div id="canvas-container"></div>

</div>

<script>

// -------- Typed.js --------
var typed = new Typed("#typed", {
    strings: ["🏠 Interactive 3D House", "Rotate • Zoom • Explore", "Smart Visualization"],
    typeSpeed: 50,
    backSpeed: 25,
    loop: true
});

// -------- Three.js Scene --------
let scene = new THREE.Scene();

let camera = new THREE.PerspectiveCamera(75, 600/350, 0.1, 1000);

let renderer = new THREE.WebGLRenderer({ antialias:true });
renderer.setSize(600,350);

document.getElementById("canvas-container").appendChild(renderer.domElement);

// Controls
let controls = new THREE.OrbitControls(camera, renderer.domElement);

// Lights
let light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5,5,5);
scene.add(light);

// Ambient light (NEW - smoother look)
let ambient = new THREE.AmbientLight(0x404040);
scene.add(ambient);

// House Base
let house = new THREE.Mesh(
    new THREE.BoxGeometry(2,1,2),
    new THREE.MeshStandardMaterial({color:0x8B4513})
);
scene.add(house);

// Roof
let roof = new THREE.Mesh(
    new THREE.ConeGeometry(1.5,1,4),
    new THREE.MeshStandardMaterial({color:0xff4d4d})
);
roof.position.y = 1;
roof.rotation.y = Math.PI/4;
scene.add(roof);

// Door (NEW)
let door = new THREE.Mesh(
    new THREE.BoxGeometry(0.5,0.7,0.1),
    new THREE.MeshStandardMaterial({color:0x654321})
);
door.position.set(0,-0.15,1.01);
scene.add(door);

// Ground
let ground = new THREE.Mesh(
    new THREE.PlaneGeometry(10,10),
    new THREE.MeshStandardMaterial({color:0x1e7e34})
);
ground.rotation.x = -Math.PI/2;
ground.position.y = -1;
scene.add(ground);

// Camera position
camera.position.set(3,3,5);

// Animation
function animate(){
    requestAnimationFrame(animate);

    // subtle rotation (NEW)
    house.rotation.y += 0.002;
    roof.rotation.y += 0.002;

    controls.update();
    renderer.render(scene,camera);
}

animate();

</script>

</body>
</html>
""", height=420)
