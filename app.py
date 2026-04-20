import streamlit as st
import streamlit.components.v1 as components
import math

# ============================================================
#  PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="الانعكاس الكلي الداخلي | Total Internal Reflection",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
#  CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap');

    :root {
        --bg: #070b14;
        --card: #0d1525;
        --card-border: #1a2744;
        --accent: #00e5a0;
        --accent2: #00b8ff;
        --laser: #ff2244;
        --text: #e8ecf4;
        --muted: #7a8ba8;
        --gold: #ffc857;
    }

    * { font-family: 'Cairo', sans-serif; }

    .stApp {
        background: var(--bg);
        color: var(--text);
    }

    .main-header {
        background: linear-gradient(135deg, #0d1525 0%, #0a1628 50%, #0d1525 100%);
        border: 1px solid var(--card-border);
        border-radius: 16px;
        padding: 28px 36px;
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }

    .main-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(ellipse at 30% 50%, rgba(0,229,160,0.04) 0%, transparent 60%),
                    radial-gradient(ellipse at 70% 50%, rgba(0,184,255,0.04) 0%, transparent 60%);
        pointer-events: none;
    }

    .header-title {
        font-size: 2rem;
        font-weight: 900;
        background: linear-gradient(135deg, var(--accent), var(--accent2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
        position: relative;
    }

    .header-sub {
        font-size: 1rem;
        color: var(--muted);
        font-weight: 400;
    }

    .author-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(0,229,160,0.15), rgba(0,184,255,0.15));
        border: 1px solid rgba(0,229,160,0.3);
        border-radius: 10px;
        padding: 8px 20px;
        margin-top: 12px;
        font-size: 0.85rem;
        color: var(--accent);
        font-weight: 600;
    }

    .glass-card {
        background: var(--card);
        border: 1px solid var(--card-border);
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 16px;
    }

    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: var(--accent);
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .section-title .icon {
        font-size: 1.5rem;
    }

    .formula-box {
        background: linear-gradient(135deg, rgba(0,229,160,0.08), rgba(0,184,255,0.08));
        border: 1px solid rgba(0,229,160,0.25);
        border-radius: 10px;
        padding: 16px 24px;
        text-align: center;
        font-size: 1.25rem;
        font-weight: 600;
        color: #fff;
        margin: 12px 0;
        direction: ltr;
        font-family: 'Courier New', monospace;
        letter-spacing: 1px;
    }

    .condition-box {
        background: rgba(255,200,87,0.08);
        border: 1px solid rgba(255,200,87,0.3);
        border-radius: 10px;
        padding: 14px 20px;
        margin: 10px 0;
    }

    .condition-box .cond-title {
        color: var(--gold);
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 6px;
    }

    .condition-box ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }

    .condition-box ul li {
        padding: 4px 0;
        padding-right: 18px;
        position: relative;
        color: var(--text);
        font-size: 0.9rem;
    }

    .condition-box ul li::before {
        content: '◆';
        position: absolute;
        right: 0;
        color: var(--gold);
        font-size: 0.6rem;
        top: 7px;
    }

    .result-badge {
        display: inline-block;
        padding: 6px 18px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 0.95rem;
    }

    .badge-refraction {
        background: rgba(0,184,255,0.15);
        border: 1px solid rgba(0,184,255,0.4);
        color: var(--accent2);
    }

    .badge-critical {
        background: rgba(255,200,87,0.15);
        border: 1px solid rgba(255,200,87,0.4);
        color: var(--gold);
    }

    .badge-tir {
        background: rgba(255,34,68,0.15);
        border: 1px solid rgba(255,34,68,0.4);
        color: var(--laser);
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background: var(--card);
        border: 1px solid var(--card-border);
        border-radius: 10px;
        padding: 10px 18px;
        color: var(--muted);
        font-family: 'Cairo', sans-serif;
        font-weight: 600;
        font-size: 0.85rem;
    }

    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0,229,160,0.15), rgba(0,184,255,0.15));
        border-color: var(--accent);
        color: var(--accent);
    }

    .stTabs [data-baseweb="tab-panel"] {
        background: transparent;
    }

    .stSelectbox label, .stSlider label, .stNumberInput label {
        color: var(--text) !important;
        font-weight: 600 !important;
    }

    .stSelectbox div[data-baseweb="select"], .stNumberInput input {
        background: var(--card) !important;
        border-color: var(--card-border) !important;
        color: var(--text) !important;
    }

    .stSlider > div > div > div {
        background: linear-gradient(90deg, var(--accent), var(--accent2)) !important;
    }

    .exp-step {
        background: rgba(0,229,160,0.05);
        border-right: 3px solid var(--accent);
        padding: 12px 18px;
        margin: 8px 0;
        border-radius: 0 8px 8px 0;
    }

    .exp-step-num {
        display: inline-block;
        background: var(--accent);
        color: var(--bg);
        width: 26px;
        height: 26px;
        border-radius: 50%;
        text-align: center;
        line-height: 26px;
        font-weight: 700;
        font-size: 0.8rem;
        margin-left: 8px;
    }

    .quiz-option {
        background: var(--card);
        border: 1px solid var(--card-border);
        border-radius: 10px;
        padding: 12px 18px;
        margin: 6px 0;
        cursor: pointer;
        transition: all 0.2s;
    }

    .quiz-option:hover {
        border-color: var(--accent);
        background: rgba(0,229,160,0.05);
    }

    .quiz-correct {
        border-color: var(--accent) !important;
        background: rgba(0,229,160,0.12) !important;
    }

    .quiz-wrong {
        border-color: var(--laser) !important;
        background: rgba(255,34,68,0.12) !important;
    }

    .phenomenon-card {
        background: var(--card);
        border: 1px solid var(--card-border);
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 20px;
    }

    .phenomenon-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .info-row {
        display: flex;
        gap: 12px;
        align-items: center;
        padding: 8px 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    .info-label {
        color: var(--muted);
        font-size: 0.85rem;
        min-width: 100px;
    }

    .info-value {
        color: var(--text);
        font-weight: 600;
        font-size: 0.95rem;
        direction: ltr;
    }

    @media (max-width: 768px) {
        .header-title { font-size: 1.4rem; }
        .main-header { padding: 18px 20px; }
        .glass-card { padding: 16px; }
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
#  HELPER FUNCTIONS
# ============================================================
def calc_critical_angle(n1, n2):
    """Calculate critical angle. Returns None if TIR is impossible."""
    if n1 <= n2:
        return None
    ratio = n2 / n1
    if ratio > 1:
        return None
    return math.degrees(math.asin(ratio))


def calc_refraction_angle(n1, theta1_deg, n2):
    """Calculate refraction angle using Snell's law. Returns None if TIR."""
    sin_theta2 = n1 * math.sin(math.radians(theta1_deg)) / n2
    if abs(sin_theta2) > 1:
        return None
    return math.degrees(math.asin(sin_theta2))


# ============================================================
#  THREE.JS 3D TIR SIMULATION TEMPLATE  (المصححة)
# ============================================================
def get_tir_3d_html(angle_deg, n1, n2):
    theta_c = calc_critical_angle(n1, n2)
    theta_c_str = f"{theta_c:.1f}" if theta_c is not None else "N/A"
    theta2 = calc_refraction_angle(n1, angle_deg, n2)
    theta2_str = f"{theta2:.1f}" if theta2 is not None else "N/A"

    if theta_c is not None:
        if angle_deg < theta_c - 0.3:
            mode = "refraction"
        elif angle_deg > theta_c + 0.3:
            mode = "reflection"
        else:
            mode = "critical"
    else:
        mode = "refraction"
        theta2_str = f"{theta2:.1f}" if theta2 is not None else "N/A"

    html = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:#070b14;font-family:'Cairo',Arial,sans-serif}
canvas{display:block;width:100%;height:100%}
.label-3d{position:absolute;color:#e8ecf4;font-size:13px;font-weight:600;pointer-events:none;white-space:nowrap;text-shadow:0 0 8px rgba(0,0,0,0.9);transform:translate(-50%,-50%)}
.label-n1{color:#00b8ff;font-size:14px}
.label-n2{color:#88aacc;font-size:14px}
.label-angle{color:#ffc857;font-size:12px}
.label-normal{color:rgba(255,255,255,0.5);font-size:11px}
.label-mode{position:absolute;bottom:12px;left:50%;transform:translateX(-50%);padding:8px 22px;border-radius:10px;font-size:13px;font-weight:700;pointer-events:none;white-space:nowrap}
.mode-refraction{background:rgba(0,184,255,0.2);border:1px solid rgba(0,184,255,0.5);color:#00b8ff}
.mode-critical{background:rgba(255,200,87,0.2);border:1px solid rgba(255,200,87,0.5);color:#ffc857}
.mode-reflection{background:rgba(255,34,68,0.2);border:1px solid rgba(255,34,68,0.5);color:#ff2244}
.info-panel{position:absolute;top:10px;right:10px;background:rgba(13,21,37,0.88);border:1px solid rgba(26,39,68,0.8);border-radius:10px;padding:10px 14px;direction:rtl;font-size:11px;color:#a0b0c8;line-height:1.9;pointer-events:none}
.info-panel .val{color:#fff;font-weight:700;direction:ltr;display:inline-block}
.info-panel .accent{color:#00e5a0}
#loadingMsg{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#7a8ba8;font-size:14px}
</style>
</head>
<body>
<div id="loadingMsg">\u062C\u0627\u0631\u064A \u062A\u062D\u0645\u064A\u0644 \u0627\u0644\u0645\u062D\u0627\u0643\u0627\u0629...</div>
<div class="info-panel" id="infoPanel"></div>
<div class="label-mode" id="modeLabel"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
window.addEventListener('load', function(){
    var loadMsg = document.getElementById('loadingMsg');
    if(loadMsg) loadMsg.style.display = 'none';

    if(typeof THREE === 'undefined'){
        document.body.innerHTML = '<div style="color:#ff4466;text-align:center;padding:40px;font-size:16px">\u062A\u0639\u0630\u0631 \u062A\u062D\u0645\u064A\u0644 \u0645\u0643\u062A\u0628\u0629 Three.js</div>';
        return;
    }

    var W = window.innerWidth;
    var H = window.innerHeight;
    if(W < 100) W = 700;
    if(H < 100) H = 520;

    var ANGLE = """ + str(angle_deg) + """;
    var N1 = """ + str(n1) + """;
    var N2 = """ + str(n2) + """;
    var THETA_C = """ + theta_c_str + """;
    var THETA2 = """ + theta2_str + """;
    var MODE = '""" + mode + """';

    var scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070b14);

    var camera = new THREE.PerspectiveCamera(42, W/H, 0.1, 100);
    var camDist = 9;
    var rotX = 0.35, rotY = 0.75;

    function updateCamera(){
        camera.position.x = camDist * Math.sin(rotY) * Math.cos(rotX);
        camera.position.y = camDist * Math.sin(rotX);
        camera.position.z = camDist * Math.cos(rotY) * Math.cos(rotX);
        camera.lookAt(0, -0.3, 0);
    }
    updateCamera();

    var renderer = new THREE.WebGLRenderer({antialias:true});
    renderer.setSize(W, H);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    document.body.insertBefore(renderer.domElement, document.body.firstChild);

    scene.add(new THREE.AmbientLight(0x405070, 0.7));
    var dLight = new THREE.DirectionalLight(0xffffff, 0.6);
    dLight.position.set(4, 8, 6);
    scene.add(dLight);
    var pLight = new THREE.PointLight(0xff2244, 0.4, 10);
    pLight.position.set(0, 0, 0.5);
    scene.add(pLight);

    var m1Geo = new THREE.BoxGeometry(7, 2.5, 4);
    var m1Mat = new THREE.MeshPhysicalMaterial({color:0x1a6baa, transparent:true, opacity:0.12, side:THREE.DoubleSide, depthWrite:false});
    var m1 = new THREE.Mesh(m1Geo, m1Mat);
    m1.position.y = -1.25;
    scene.add(m1);
    var m1E = new THREE.LineSegments(new THREE.EdgesGeometry(m1Geo), new THREE.LineBasicMaterial({color:0x2288cc, transparent:true, opacity:0.35}));
    m1E.position.y = -1.25;
    scene.add(m1E);

    var m2Geo = new THREE.BoxGeometry(7, 2.5, 4);
    var m2Mat = new THREE.MeshPhysicalMaterial({color:0x445566, transparent:true, opacity:0.03, side:THREE.DoubleSide, depthWrite:false});
    var m2 = new THREE.Mesh(m2Geo, m2Mat);
    m2.position.y = 1.25;
    scene.add(m2);
    var m2E = new THREE.LineSegments(new THREE.EdgesGeometry(m2Geo), new THREE.LineBasicMaterial({color:0x334455, transparent:true, opacity:0.2}));
    m2E.position.y = 1.25;
    scene.add(m2E);

    var grid = new THREE.GridHelper(7, 14, 0x00e5a0, 0x00e5a0);
    grid.material.transparent = true;
    grid.material.opacity = 0.08;
    scene.add(grid);
    var bPlane = new THREE.Mesh(new THREE.PlaneGeometry(7,4), new THREE.MeshBasicMaterial({color:0x00e5a0, transparent:true, opacity:0.04, side:THREE.DoubleSide, depthWrite:false}));
    bPlane.rotation.x = -Math.PI/2;
    scene.add(bPlane);

    var nGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0,-2.8,0), new THREE.Vector3(0,2.8,0)]);
    var nLine = new THREE.Line(nGeo, new THREE.LineDashedMaterial({color:0xffffff, dashSize:0.12, gapSize:0.08, transparent:true, opacity:0.3}));
    nLine.computeLineDistances();
    scene.add(nLine);

    function makeBeam(s, e, col, gcol){
        var d = new THREE.Vector3().subVectors(e, s);
        var len = Math.max(0.001, d.length());
        var mid = new THREE.Vector3().addVectors(s, e).multiplyScalar(0.5);
        var g = new THREE.Group();
        var dir = d.clone().normalize();
        var core = new THREE.Mesh(new THREE.CylinderGeometry(0.018,0.018,len,8), new THREE.MeshBasicMaterial({color:col}));
        core.position.copy(mid);
        core.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0), dir);
        g.add(core);
        var gl = new THREE.Mesh(new THREE.CylinderGeometry(0.06,0.06,len,8), new THREE.MeshBasicMaterial({color:gcol, transparent:true, opacity:0.18, depthWrite:false}));
        gl.position.copy(mid);
        gl.quaternion.copy(core.quaternion);
        g.add(gl);
        var gl2 = new THREE.Mesh(new THREE.CylinderGeometry(0.13,0.13,len,8), new THREE.MeshBasicMaterial({color:gcol, transparent:true, opacity:0.05, depthWrite:false}));
        gl2.position.copy(mid);
        gl2.quaternion.copy(core.quaternion);
        g.add(gl2);
        return g;
    }

    function makeArc(ctr, r, sa, ea, col){
        var pts = [];
        for(var i=0;i<=40;i++){
            var a = sa + (ea-sa)*i/40;
            pts.push(new THREE.Vector3(ctr.x+Math.cos(a)*r, ctr.y+Math.sin(a)*r, 0));
        }
        return new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), new THREE.LineBasicMaterial({color:col, transparent:true, opacity:0.8}));
    }

    var aRad = ANGLE * Math.PI / 180;
    var rL = 2.8;

    var incS = new THREE.Vector3(-Math.sin(aRad)*rL, -Math.cos(aRad)*rL, 0);
    var incE = new THREE.Vector3(0, 0, 0);
    scene.add(makeBeam(incS, incE, 0xff2244, 0xff4466));

    if(MODE === 'refraction'){
        var t2 = parseFloat(THETA2) * Math.PI / 180;
        var refE = new THREE.Vector3(Math.sin(t2)*rL, Math.cos(t2)*rL, 0);
        scene.add(makeBeam(incE, refE, 0x00b8ff, 0x0088cc));
        var rEnd = new THREE.Vector3(Math.sin(aRad)*rL*0.4, -Math.cos(aRad)*rL*0.4, 0);
        var wb = makeBeam(incE, rEnd, 0xff2244, 0xff2244);
        wb.children.forEach(function(c){c.material.opacity *= 0.2;});
        scene.add(wb);
    } else if(MODE === 'critical'){
        var cEnd = new THREE.Vector3(rL, 0, 0);
        scene.add(makeBeam(incE, cEnd, 0xffc857, 0xffc857));
    } else {
        var rlE = new THREE.Vector3(Math.sin(aRad)*rL, -Math.cos(aRad)*rL, 0);
        scene.add(makeBeam(incE, rlE, 0xff2244, 0xff4466));
    }

    var incArcEnd = Math.atan2(-Math.cos(aRad), -Math.sin(aRad));
    scene.add(makeArc(new THREE.Vector3(0,0,0), 0.8, -Math.PI/2, incArcEnd, 0xffc857));
    if(MODE === 'refraction' && THETA2 !== 'N/A'){
        var t2a = parseFloat(THETA2)*Math.PI/180;
        scene.add(makeArc(new THREE.Vector3(0,0,0), 0.7, Math.atan2(Math.cos(t2a),Math.sin(t2a)), Math.PI/2, 0x00b8ff));
    }
    if(MODE === 'reflection'){
        scene.add(makeArc(new THREE.Vector3(0,0,0), 0.7, -Math.PI/2, Math.atan2(-Math.cos(aRad),Math.sin(aRad)), 0xff6688));
    }

    var hitM = new THREE.MeshBasicMaterial({color:0xff4466, transparent:true, opacity:0.6});
    scene.add(new THREE.Mesh(new THREE.SphereGeometry(0.06,16,16), hitM));

    function addLbl(text, p3, cls){
        var d = document.createElement('div');
        d.className = 'label-3d ' + (cls||'');
        d.textContent = text;
        document.body.appendChild(d);
        return {div:d, pos:p3};
    }
    var lbls = [
        addLbl('n\u2081 = '+N1.toFixed(2), new THREE.Vector3(-2.5,-1.2,2.1), 'label-n1'),
        addLbl('n\u2082 = '+N2.toFixed(2), new THREE.Vector3(-2.5,1.5,2.1), 'label-n2'),
        addLbl('N (Normal)', new THREE.Vector3(0.3,2.2,0), 'label-normal'),
        addLbl('\u03B8\u2081 = '+ANGLE.toFixed(1)+'\u00B0', new THREE.Vector3(-0.9,-0.6,0), 'label-angle')
    ];
    if(MODE === 'refraction' && THETA2 !== 'N/A'){
        lbls.push(addLbl('\u03B8\u2082 = '+parseFloat(THETA2).toFixed(1)+'\u00B0', new THREE.Vector3(0.8,0.5,0), 'label-angle'));
    }
    if(MODE === 'critical'){
        lbls.push(addLbl('\u03B8\u2082 = 90\u00B0', new THREE.Vector3(1.5,0.3,0), 'label-angle'));
    }
    if(MODE === 'reflection'){
        lbls.push(addLbl("\u03B8' = "+ANGLE.toFixed(1)+'\u00B0', new THREE.Vector3(0.9,-0.6,0), 'label-angle'));
    }

    var modeLbl = document.getElementById('modeLabel');
    if(MODE === 'refraction'){
        modeLbl.className = 'label-mode mode-refraction';
        modeLbl.textContent = '\u0627\u0646\u0643\u0633\u0627\u0631 Refraction (\u03B8\u2081 < \u03B8c)';
    } else if(MODE === 'critical'){
        modeLbl.className = 'label-mode mode-critical';
        modeLbl.textContent = '\u0627\u0644\u0632\u0627\u0648\u064A\u0629 \u0627\u0644\u062D\u0631\u062C\u0629 Critical Angle (\u03B8\u2081 = \u03B8c)';
    } else {
        modeLbl.className = 'label-mode mode-reflection';
        modeLbl.textContent = '\u0627\u0646\u0639\u0643\u0627\u0633 \u0643\u0644\u064A \u062F\u0627\u062E\u0644\u064A TIR (\u03B8\u2081 > \u03B8c)';
    }

    document.getElementById('infoPanel').innerHTML =
        "Snell's Law: n\u2081 sin \u03B8\u2081 = n\u2082 sin \u03B8\u2082<br>"+
        "n\u2081 = <span class='val'>"+N1.toFixed(2)+"</span><br>"+
        "n\u2082 = <span class='val'>"+N2.toFixed(2)+"</span><br>"+
        "\u03B8c = <span class='val accent'>"+THETA_C+"\u00B0</span><br>"+
        "\u03B8\u2081 = <span class='val'>"+ANGLE.toFixed(1)+"\u00B0</span><br>"+
        "\u03B8\u2082 = <span class='val'>"+THETA2+"\u00B0</span>";

    var isDrag = false, prevMX = 0, prevMY = 0;
    var canvas = renderer.domElement;
    canvas.style.cursor = 'grab';
    canvas.addEventListener('mousedown', function(e){isDrag=true;prevMX=e.clientX;prevMY=e.clientY;canvas.style.cursor='grabbing';});
    canvas.addEventListener('mousemove', function(e){
        if(!isDrag) return;
        rotY += (e.clientX-prevMX)*0.005;
        rotX += (e.clientY-prevMY)*0.005;
        rotX = Math.max(-1.2, Math.min(1.2, rotX));
        prevMX=e.clientX; prevMY=e.clientY;
    });
    canvas.addEventListener('mouseup', function(){isDrag=false;canvas.style.cursor='grab';});
    canvas.addEventListener('mouseleave', function(){isDrag=false;canvas.style.cursor='grab';});
    canvas.addEventListener('wheel', function(e){
        camDist += e.deltaY*0.01;
        camDist = Math.max(4, Math.min(18, camDist));
    });
    canvas.addEventListener('touchstart', function(e){
        if(e.touches.length===1){isDrag=true;prevMX=e.touches[0].clientX;prevMY=e.touches[0].clientY;}
    });
    canvas.addEventListener('touchmove', function(e){
        if(!isDrag||e.touches.length!==1) return;
        e.preventDefault();
        rotY += (e.touches[0].clientX-prevMX)*0.005;
        rotX += (e.touches[0].clientY-prevMY)*0.005;
        rotX = Math.max(-1.2, Math.min(1.2, rotX));
        prevMX=e.touches[0].clientX; prevMY=e.touches[0].clientY;
    }, {passive:false});
    canvas.addEventListener('touchend', function(){isDrag=false;});

    function toScreen(pos){
        var v = pos.clone().project(camera);
        return {x:(v.x*0.5+0.5)*W, y:(-v.y*0.5+0.5)*H};
    }

    var time = 0;
    function animate(){
        requestAnimationFrame(animate);
        time += 0.02;
        updateCamera();
        hitM.opacity = 0.4 + 0.3*Math.sin(time*3);
        pLight.intensity = 0.3 + 0.2*Math.sin(time*3);
        lbls.forEach(function(l){
            var s = toScreen(l.pos);
            l.div.style.left = s.x+'px';
            l.div.style.top = s.y+'px';
        });
        renderer.render(scene, camera);
    }
    animate();

    window.addEventListener('resize', function(){
        W = window.innerWidth; H = window.innerHeight;
        if(W<100) W=700; if(H<100) H=520;
        camera.aspect = W/H;
        camera.updateProjectionMatrix();
        renderer.setSize(W, H);
    });
});
</script>
</body></html>"""
    return html


# ============================================================
#  RAINBOW TEMPLATE (بدون تعديل - تعمل بشكل ممتاز)
# ============================================================
def get_rainbow_html():
    return """<!DOCTYPE html>
<html dir="rtl"><head><meta charset="UTF-8">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#070b14; overflow:hidden; font-family:'Cairo',Arial,sans-serif; }
#container { width:100%; height:100%; position:relative; }
canvas { display:block; width:100%; height:100%; }
.legend { position:absolute; bottom:10px; right:10px; background:rgba(13,21,37,0.9);
border:1px solid #1a2744; border-radius:10px; padding:10px 16px; color:#a0b0c8; font-size:11px; line-height:1.7; }
.legend .c { display:inline-block; width:12px; height:12px; border-radius:2px; margin-left:6px; vertical-align:middle; }
</style></head><body>
<div id="container"><canvas id="cv"></canvas>
<div class="legend">
<div><span class="c" style="background:#ff0000"></span>Red (n=1.331)</div>
<div><span class="c" style="background:#ff7700"></span>Orange (n=1.332)</div>
<div><span class="c" style="background:#ffff00"></span>Yellow (n=1.333)</div>
<div><span class="c" style="background:#00ff00"></span>Green (n=1.335)</div>
<div><span class="c" style="background:#0088ff"></span>Blue (n=1.338)</div>
<div><span class="c" style="background:#4400ff"></span>Indigo (n=1.340)</div>
<div><span class="c" style="background:#8800ff"></span>Violet (n=1.342)</div>
</div></div>
<script>
window.addEventListener('load', function(){
var cv = document.getElementById('cv');
var ctx = cv.getContext('2d');
var container = document.getElementById('container');
var W = container.clientWidth;
var H = container.clientHeight;
if(W < 100) W = 700;
if(H < 100) H = 480;
cv.width = W; cv.height = H;
var cx = W * 0.45, cy = H * 0.48, R = Math.min(W, H) * 0.28;
if(R < 30) R = 120;
var time = 0;

var colors = [
    {name:'Red', hex:'#ff2233', n:1.331, angle:42.0},
    {name:'Orange', hex:'#ff8811', n:1.332, angle:42.3},
    {name:'Yellow', hex:'#ffdd00', n:1.333, angle:42.6},
    {name:'Green', hex:'#00dd44', n:1.335, angle:43.2},
    {name:'Blue', hex:'#0088ff', n:1.338, angle:44.1},
    {name:'Indigo', hex:'#4400ee', n:1.340, angle:44.8},
    {name:'Violet', hex:'#9900ff', n:1.342, angle:45.5}
];

function drawDrop(){
    var grad = ctx.createRadialGradient(cx-R*0.2, cy-R*0.2, R*0.1, cx, cy, R);
    grad.addColorStop(0, 'rgba(100,180,255,0.12)');
    grad.addColorStop(0.7, 'rgba(60,130,220,0.08)');
    grad.addColorStop(1, 'rgba(30,80,180,0.15)');
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, Math.PI*2);
    ctx.fillStyle = grad; ctx.fill();
    ctx.strokeStyle = 'rgba(100,180,255,0.35)'; ctx.lineWidth = 2; ctx.stroke();
    ctx.beginPath(); ctx.arc(cx - R*0.25, cy - R*0.3, R*0.15, 0, Math.PI*2);
    ctx.fillStyle = 'rgba(255,255,255,0.06)'; ctx.fill();
}

function calcRefraction(n1, theta1, n2){
    var s = n1 * Math.sin(theta1) / n2;
    if(Math.abs(s)>1) return null;
    return Math.asin(s);
}

function drawRays(t){
    var entryAngle = 0.6;
    var entryX = cx - R * Math.cos(entryAngle);
    var entryY = cy - R * Math.sin(entryAngle);

    ctx.beginPath(); ctx.moveTo(entryX - 120, entryY - 120 * Math.tan(entryAngle)); ctx.lineTo(entryX, entryY);
    ctx.strokeStyle = 'rgba(255,255,255,0.7)'; ctx.lineWidth = 2.5; ctx.stroke();
    ctx.beginPath(); ctx.moveTo(entryX - 120, entryY - 120 * Math.tan(entryAngle)); ctx.lineTo(entryX, entryY);
    ctx.strokeStyle = 'rgba(255,255,255,0.1)'; ctx.lineWidth = 8; ctx.stroke();

    ctx.fillStyle = '#fff'; ctx.font = '12px Cairo';
    ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
    ctx.fillText('A', entryX - 18, entryY - 8);

    var nx = (cx - entryX), ny = (cy - entryY);
    var nLen = Math.sqrt(nx*nx + ny*ny);
    nx /= nLen; ny /= nLen;
    ctx.beginPath(); ctx.setLineDash([4,4]);
    ctx.moveTo(entryX - nx*40, entryY - ny*40);
    ctx.lineTo(entryX + nx*40, entryY + ny*40);
    ctx.strokeStyle = 'rgba(255,255,255,0.25)'; ctx.lineWidth = 1; ctx.stroke();
    ctx.setLineDash([]);

    var backX = cx + R * Math.cos(entryAngle * 0.3);
    var backY = cy + R * Math.sin(entryAngle * 0.2);
    ctx.fillStyle = '#fff'; ctx.font = '12px Cairo';
    ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
    ctx.fillText('B', backX + 8, backY - 8);

    colors.forEach(function(col, i){
        var ref1 = calcRefraction(1.0, entryAngle, col.n);
        if(ref1 === null) return;
        var bxDiff = R * 0.85 * (0.3 + i * 0.02);
        var byDiff = R * 0.5;
        var bx = cx + bxDiff;
        var by = cy + byDiff * (0.9 + i*0.01);
        ctx.beginPath(); ctx.moveTo(entryX, entryY); ctx.lineTo(bx, by);
        ctx.strokeStyle = col.hex + '80'; ctx.lineWidth = 1.5; ctx.stroke();
        var exitX = cx + R * Math.cos((0.8 + i*0.05) * (Math.PI/2));
        var exitY = cy - R * Math.sin((0.8 + i*0.05) * (Math.PI/2));
        ctx.beginPath(); ctx.moveTo(bx, by); ctx.lineTo(exitX, exitY);
        ctx.strokeStyle = col.hex + '60'; ctx.lineWidth = 1.5; ctx.stroke();
        ctx.fillStyle = '#fff'; ctx.font = '10px Cairo';
        ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
        ctx.fillText('C', exitX + 6, exitY - 4);
        var exitAngle = col.angle * Math.PI / 180;
        var exitEndX = exitX + 100 * Math.cos(exitAngle + Math.PI * 0.3);
        var exitEndY = exitY - 100 * Math.sin(exitAngle + Math.PI * 0.15);
        var progress = ((t * 0.5 + i * 0.15) % 1.5);
        var pLen = Math.min(progress, 1);
        ctx.beginPath(); ctx.moveTo(exitX, exitY);
        ctx.lineTo(exitX + (exitEndX - exitX) * pLen, exitY + (exitEndY - exitY) * pLen);
        ctx.strokeStyle = col.hex; ctx.lineWidth = 2; ctx.stroke();
        ctx.beginPath(); ctx.moveTo(exitX, exitY);
        ctx.lineTo(exitX + (exitEndX - exitX) * pLen, exitY + (exitEndY - exitY) * pLen);
        ctx.strokeStyle = col.hex + '30'; ctx.lineWidth = 6; ctx.stroke();
    });

    ctx.fillStyle = '#ff2244'; ctx.font = 'bold 11px Cairo';
    ctx.textAlign = 'left'; ctx.textBaseline = 'middle';
    ctx.fillText('TIR', backX + 8, backY + 14);
}

function drawLabels(){
    ctx.fillStyle = '#00e5a0'; ctx.font = 'bold 14px Cairo';
    ctx.textAlign = 'center'; ctx.textBaseline = 'top';
    ctx.fillText('\u062A\u062D\u0644\u064A\u0644 \u0636\u0648\u0621 \u0627\u0644\u0634\u0645\u0633 \u0639\u0628\u0631 \u0642\u0637\u0631\u0629 \u0645\u0637\u0631', cx, 24);
    ctx.textAlign = 'right'; ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = '#7a8ba8'; ctx.font = '12px Cairo';
    var info = [
        '\u2022 \u064A\u0646\u0643\u0633\u0631 \u0627\u0644\u0636\u0648\u0621 \u0639\u0646\u062F \u0627\u0644\u0646\u0642\u0637\u0629 A (\u062F\u062E\u0648\u0644 \u0627\u0644\u0642\u0637\u0631\u0629)',
        '\u2022 \u064A\u0646\u0639\u0643\u0633 \u0627\u0646\u0639\u0643\u0627\u0633\u0627\u064B \u0643\u0644\u064A\u0627\u064B \u062F\u0627\u062E\u0644\u064A\u0627\u064B \u0639\u0646\u062F \u0627\u0644\u0646\u0642\u0637\u0629 B',
        '\u2022 \u064A\u0646\u0643\u0633\u0631 \u0645\u0628\u062A\u0639\u062F\u0627\u064B \u0639\u0646 \u0627\u0644\u0639\u0645\u0648\u062F \u0639\u0646\u062F \u0627\u0644\u0646\u0642\u0637\u0629 C',
        '\u2022 \u0643\u0644 \u0644\u0648\u0646 \u0644\u0647 \u0645\u0639\u0627\u0645\u0644 \u0627\u0646\u0643\u0633\u0627\u0631 \u0645\u062E\u062A\u0644\u0641 \u0641\u064A \u0627\u0644\u0645\u0627\u0621'
    ];
    info.forEach(function(line, i){
        ctx.fillText(line, W - 20, H - 120 + i * 22);
    });
}

function animate(){
    time += 0.016;
    ctx.clearRect(0, 0, W, H);
    drawDrop();
    drawRays(time);
    drawLabels();
    requestAnimationFrame(animate);
}
animate();

window.addEventListener('resize', function(){
    W = container.clientWidth; H = container.clientHeight;
    if(W < 100) W = 700; if(H < 100) H = 480;
    cv.width = W; cv.height = H;
    cx = W * 0.45; cy = H * 0.48; R = Math.min(W, H) * 0.28;
    if(R < 30) R = 120;
});
});
</script></body></html>"""


# ============================================================
#  FIBER OPTICS TEMPLATE (بدون تعديل - تعمل بشكل ممتاز)
# ============================================================
def get_fiber_html():
    return """<!DOCTYPE html>
<html dir="rtl"><head><meta charset="UTF-8">
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#070b14; overflow:hidden; font-family:'Cairo',Arial,sans-serif; }
#container { width:100%; height:100%; position:relative; }
canvas { display:block; width:100%; height:100%; }
.info { position:absolute; top:10px; right:10px; background:rgba(13,21,37,0.9);
border:1px solid #1a2744; border-radius:10px; padding:10px 16px; color:#a0b0c8; font-size:11px; line-height:1.8; }
.info .v { color:#00e5a0; font-weight:700; }
</style></head><body>
<div id="container"><canvas id="cv"></canvas>
<div class="info">
\u0645\u0639\u0627\u0645\u0644 \u0627\u0646\u0643\u0633\u0627\u0631 \u0627\u0644\u0642\u0644\u0628: <span class="v">1.50</span><br>
\u0645\u0639\u0627\u0645\u0644 \u0627\u0646\u0643\u0633\u0627\u0631 \u0627\u0644\u063A\u0644\u0627\u0641: <span class="v">1.45</span><br>
\u0627\u0644\u0632\u0627\u0648\u064A\u0629 \u0627\u0644\u062D\u0631\u062C\u0629: <span class="v">75.2\u00B0</span>
</div></div>
<script>
window.addEventListener('load', function(){
var cv = document.getElementById('cv');
var ctx = cv.getContext('2d');
var container = document.getElementById('container');
var W = container.clientWidth;
var H = container.clientHeight;
if(W < 100) W = 700;
if(H < 100) H = 440;
cv.width = W; cv.height = H;
var time = 0;
var pulses = [];

function getFiberPath(){
    var points = [];
    var startX = 40, endX = W - 40;
    var centerY = H * 0.55;
    var amplitude = 60;
    var steps = 200;
    for(var i=0; i<=steps; i++){
        var t = i / steps;
        var x = startX + (endX - startX) * t;
        var y = centerY + Math.sin(t * Math.PI * 2.5) * amplitude + Math.sin(t * Math.PI * 1.2) * 20;
        points.push({x:x, y:y});
    }
    return points;
}

function drawFiber(path){
    var coreWidth = 28, cladWidth = 44;
    ctx.beginPath();
    ctx.moveTo(path[0].x, path[0].y - cladWidth/2);
    for(var i=1; i<path.length; i++) ctx.lineTo(path[i].x, path[i].y - cladWidth/2);
    for(var i=path.length-1; i>=0; i--) ctx.lineTo(path[i].x, path[i].y + cladWidth/2);
    ctx.closePath();
    ctx.fillStyle = 'rgba(40,60,90,0.2)'; ctx.fill();
    ctx.strokeStyle = 'rgba(60,100,150,0.3)'; ctx.lineWidth = 1; ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(path[0].x, path[0].y - coreWidth/2);
    for(var i=1; i<path.length; i++) ctx.lineTo(path[i].x, path[i].y - coreWidth/2);
    for(var i=path.length-1; i>=0; i--) ctx.lineTo(path[i].x, path[i].y + coreWidth/2);
    ctx.closePath();
    ctx.fillStyle = 'rgba(0,150,255,0.06)'; ctx.fill();
    ctx.strokeStyle = 'rgba(0,180,255,0.2)'; ctx.lineWidth = 1; ctx.stroke();
    var mid = Math.floor(path.length / 2);
    ctx.fillStyle = 'rgba(0,180,255,0.6)'; ctx.font = 'bold 11px Cairo'; ctx.textAlign = 'center'; ctx.textBaseline = 'alphabetic';
    ctx.fillText('\u0627\u0644\u0642\u0644\u0628 (Core)', path[mid].x, path[mid].y - coreWidth/2 - 6);
    ctx.fillStyle = 'rgba(60,100,150,0.6)';
    ctx.fillText('\u0627\u0644\u063A\u0644\u0627\u0641 (Cladding)', path[mid].x + 80, path[mid].y - cladWidth/2 - 6);
}

function spawnPulse(){ pulses.push({ pos: 0, speed: 0.003 + Math.random()*0.001 }); }

function drawPulses(path){
    var coreW = 24;
    pulses.forEach(function(p){
        var idx = Math.floor(p.pos * (path.length - 1));
        if(idx < 0 || idx >= path.length) return;
        var pt = path[idx];
        var nextIdx = Math.min(idx + 2, path.length - 1);
        var prevIdx = Math.max(idx - 2, 0);
        var dx = path[nextIdx].x - path[prevIdx].x;
        var dy = path[nextIdx].y - path[prevIdx].y;
        var len = Math.sqrt(dx*dx + dy*dy);
        var nx = -dy / len, ny = dx / len;
        var bouncePhase = Math.sin(p.pos * Math.PI * 12) * 0.4 + 0.5;
        var offset = (bouncePhase * 2 - 1) * (coreW/2 - 3);
        var px = pt.x + nx * offset, py = pt.y + ny * offset;
        var grad = ctx.createRadialGradient(px, py, 0, px, py, 8);
        grad.addColorStop(0, 'rgba(255,34,68,0.9)');
        grad.addColorStop(0.4, 'rgba(255,68,100,0.4)');
        grad.addColorStop(1, 'rgba(255,34,68,0)');
        ctx.beginPath(); ctx.arc(px, py, 8, 0, Math.PI*2);
        ctx.fillStyle = grad; ctx.fill();
        ctx.beginPath(); ctx.arc(px, py, 2, 0, Math.PI*2);
        ctx.fillStyle = '#ff4466'; ctx.fill();
        p.pos += p.speed;
    });
    pulses = pulses.filter(function(p){ return p.pos < 1; });
}

function drawTIRIndicators(path){
    for(var i=0; i<5; i++){
        var phase = (i + 0.5) / 5;
        var idx = Math.floor(phase * (path.length - 1));
        if(idx < 2 || idx >= path.length - 2) continue;
        var pt = path[idx];
        var alpha = 0.15 + 0.1 * Math.sin(time * 2 + i);
        ctx.beginPath(); ctx.arc(pt.x, pt.y, 5, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(255,34,68,' + alpha + ')'; ctx.fill();
    }
}

function drawLabels2(){
    ctx.fillStyle = '#00e5a0'; ctx.font = 'bold 14px Cairo';
    ctx.textAlign = 'center'; ctx.textBaseline = 'top';
    ctx.fillText('\u0627\u0646\u062A\u0642\u0627\u0644 \u0627\u0644\u0636\u0648\u0621 \u0641\u064A \u0627\u0644\u0623\u0644\u064A\u0627\u0641 \u0627\u0644\u0636\u0648\u0626\u064A\u0629', W/2, 24);
    ctx.textAlign = 'right'; ctx.textBaseline = 'alphabetic';
    ctx.fillStyle = '#7a8ba8'; ctx.font = '11px Cairo';
    ctx.fillText('\u064A\u0646\u0639\u0643\u0633 \u0627\u0644\u0636\u0648\u0621 \u0627\u0646\u0639\u0643\u0627\u0633\u0627\u064B \u0643\u0644\u064A\u0627\u064B \u062F\u0627\u062E\u0644\u064A\u0627\u064B \u0628\u064A\u0646 \u0627\u0644\u0642\u0644\u0628 \u0648\u0627\u0644\u063A\u0644\u0627\u0641', W - 20, H - 16);
}

var frameCount = 0;
function animate(){
    time += 0.016; frameCount++;
    ctx.clearRect(0, 0, W, H);
    var path = getFiberPath();
    drawFiber(path);
    drawTIRIndicators(path);
    if(frameCount % 30 === 0) spawnPulse();
    drawPulses(path);
    drawLabels2();
    requestAnimationFrame(animate);
}
animate();

window.addEventListener('resize', function(){
    W = container.clientWidth; H = container.clientHeight;
    if(W < 100) W = 700; if(H < 100) H = 440;
    cv.width = W; cv.height = H;
});
});
</script></body></html>"""


# ============================================================
#  MIRAGE TEMPLATE (بدون تعديل - تعمل بشكل ممتاز)
# ============================================================
def get_mirage_html():
    return """<!DOCTYPE html>
<html dir="rtl"><head><meta charset="UTF-8">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:#070b14;font-family:'Cairo',Arial,sans-serif}
canvas{display:block;width:100%;height:100%}
.legend{position:absolute;top:10px;right:10px;background:rgba(13,21,37,0.9);
border:1px solid #1a2744;border-radius:10px;padding:10px 16px;color:#a0b0c8;font-size:11px;line-height:1.9;direction:rtl}
.legend .v{color:#ffc857;font-weight:700;direction:ltr;display:inline-block}
</style></head><body>
<canvas id="cv"></canvas>
<div class="legend">
<span class="v">n&#8324; > n&#8323; > n&#8322; > n&#8321;</span><br>
\u0643\u0644\u0645\u0627 \u0627\u0631\u062A\u0641\u0639\u0646\u0627 \u0639\u0646 \u0633\u0637\u062D \u0627\u0644\u0623\u0631\u0636:<br>
\u062A\u062A\u0646\u0627\u0642\u0635 \u0627\u0644\u062D\u0631\u0627\u0631\u0629 \u2191<br>
\u064A\u0632\u062F\u0627\u062F \u0645\u0639\u0627\u0645\u0644 \u0627\u0644\u0627\u0646\u0643\u0633\u0627\u0631 \u2191
</div>
<script>
window.addEventListener('load', function(){
    var cv = document.getElementById('cv');
    var ctx = cv.getContext('2d');
    var W = window.innerWidth;
    var H = window.innerHeight;
    if(W < 100) W = 700;
    if(H < 100) H = 440;
    cv.width = W;
    cv.height = H;
    var time = 0;

    var layers = [
        { y: 0.85, color: 'rgba(180,120,50,0.08)', n: 1.0001, label: 'n\\u2081' },
        { y: 0.70, color: 'rgba(160,100,40,0.06)', n: 1.0003, label: 'n\\u2082' },
        { y: 0.55, color: 'rgba(130,80,30,0.05)', n: 1.0008, label: 'n\\u2083' },
        { y: 0.35, color: 'rgba(100,60,20,0.04)', n: 1.0020, label: 'n\\u2084' }
    ];

    function drawScene(){
        var skyGrad = ctx.createLinearGradient(0, 0, 0, H * 0.85);
        skyGrad.addColorStop(0, 'rgba(15,25,50,0.8)');
        skyGrad.addColorStop(1, 'rgba(40,30,20,0.3)');
        ctx.fillStyle = skyGrad;
        ctx.fillRect(0, 0, W, H);

        var groundY = H * 0.85;
        var groundGrad = ctx.createLinearGradient(0, groundY, 0, H);
        groundGrad.addColorStop(0, 'rgba(160,110,50,0.25)');
        groundGrad.addColorStop(1, 'rgba(100,70,30,0.15)');
        ctx.fillStyle = groundGrad;
        ctx.fillRect(0, groundY, W, H - groundY);

        for(var i=0; i<8; i++){
            var waveX = (time * 30 + i * 120) % (W + 100) - 50;
            var waveY = groundY + 5 + Math.sin(time * 2 + i) * 3;
            ctx.beginPath();
            ctx.moveTo(waveX - 40, waveY);
            ctx.quadraticCurveTo(waveX, waveY - 6 - Math.sin(time*3+i)*3, waveX + 40, waveY);
            ctx.strokeStyle = 'rgba(255,180,80,' + (0.08 + 0.04*Math.sin(time*2+i)) + ')';
            ctx.lineWidth = 2;
            ctx.stroke();
        }

        layers.forEach(function(l){
            var y = H * l.y;
            ctx.beginPath();
            ctx.setLineDash([8, 8]);
            ctx.moveTo(0, y);
            ctx.lineTo(W, y);
            ctx.strokeStyle = 'rgba(255,200,87,0.12)';
            ctx.lineWidth = 1;
            ctx.stroke();
            ctx.setLineDash([]);
            if(l === layers[0]){
                ctx.fillStyle = l.color;
                ctx.fillRect(0, y, W, H - y);
            } else {
                var idx = layers.indexOf(l);
                var prevY = H * layers[idx-1].y;
                ctx.fillStyle = l.color;
                ctx.fillRect(0, y, W, prevY - y);
            }
            ctx.fillStyle = 'rgba(255,200,87,0.35)';
            ctx.font = '10px Cairo';
            ctx.textAlign = 'left';
            ctx.textBaseline = 'alphabetic';
            ctx.fillText(l.label + ' = ' + l.n.toFixed(4), 8, y - 4);
        });

        var objX = W * 0.15;
        var objBaseY = groundY;
        ctx.fillStyle = 'rgba(80,160,80,0.6)';
        ctx.fillRect(objX - 3, objBaseY - 70, 6, 70);
        ctx.beginPath();
        ctx.arc(objX, objBaseY - 80, 22, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(60,140,60,0.5)';
        ctx.fill();
        ctx.beginPath();
        ctx.arc(objX - 8, objBaseY - 72, 16, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(50,130,50,0.4)';
        ctx.fill();
        ctx.fillStyle = '#a0b0c8';
        ctx.font = '11px Cairo';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'alphabetic';
        ctx.fillText('\\u062C\\u0633\\u0645 \\u062D\\u0642\\u064A\\u0642\\u064A', objX, objBaseY - 105);

        var obsX = W * 0.82;
        var obsY = groundY;
        ctx.fillStyle = 'rgba(200,180,160,0.6)';
        ctx.fillRect(obsX - 4, obsY - 30, 8, 30);
        ctx.beginPath();
        ctx.arc(obsX, obsY - 38, 10, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(200,180,160,0.5)';
        ctx.fill();
        ctx.fillStyle = '#a0b0c8';
        ctx.font = '11px Cairo';
        ctx.textAlign = 'center';
        ctx.fillText('\\u0645\\u0631\\u0627\\u0642\\u0628', obsX, obsY - 55);

        drawLightRays(objX, objBaseY - 70, obsX, obsY - 35, groundY);

        var mirageAlpha = 0.2 + 0.1 * Math.sin(time * 1.5);
        ctx.save();
        ctx.globalAlpha = mirageAlpha;
        ctx.translate(objX + 200, groundY + 30);
        ctx.scale(0.6, -0.6);
        ctx.fillStyle = 'rgba(80,160,80,0.5)';
        ctx.fillRect(-3, -70, 6, 70);
        ctx.beginPath();
        ctx.arc(0, -80, 22, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(60,140,60,0.4)';
        ctx.fill();
        ctx.restore();
        ctx.fillStyle = 'rgba(255,200,87,0.5)';
        ctx.font = '11px Cairo';
        ctx.textAlign = 'center';
        ctx.fillText('\\u0635\\u0648\\u0631\\u0629 \\u0645\\u0642\\u0644\\u0648\\u0628\\u0629 (\\u0633\\u0631\\u0627\\u0628)', objX + 200, groundY + 55);

        ctx.fillStyle = '#ffc857';
        ctx.font = 'bold 14px Cairo';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'top';
        ctx.fillText('\\u0627\\u0644\\u0633\\u0631\\u0627\\u0628 \\u0627\\u0644\\u0635\\u062D\\u0631\\u0627\\u0648\\u064A - Inferior Mirage', W/2, 22);
    }

    function drawLightRays(ox, oy, ex, ey, groundY){
        var steps = 60;
        var points = [];
        for(var i=0; i<=steps; i++){
            var t = i / steps;
            var x = ox + (ex - ox) * t;
            var curveDepth = groundY - oy + 15;
            var y = oy + curveDepth * Math.sin(t * Math.PI) * 0.9;
            points.push({x:x, y:Math.min(y, groundY - 2)});
        }
        var animProgress = (time * 0.3) % 1.5;
        var drawCount = Math.floor(Math.min(animProgress, 1) * points.length);
        if(drawCount > 1){
            ctx.beginPath();
            ctx.moveTo(points[0].x, points[0].y);
            for(var i=1; i<drawCount; i++){
                ctx.lineTo(points[i].x, points[i].y);
            }
            ctx.strokeStyle = 'rgba(255,200,87,0.6)';
            ctx.lineWidth = 2;
            ctx.stroke();
            ctx.strokeStyle = 'rgba(255,200,87,0.1)';
            ctx.lineWidth = 6;
            ctx.stroke();
            if(drawCount > 2){
                var last = points[drawCount - 1];
                var prev = points[drawCount - 2];
                var angle = Math.atan2(last.y - prev.y, last.x - prev.x);
                ctx.beginPath();
                ctx.moveTo(last.x, last.y);
                ctx.lineTo(last.x - 8*Math.cos(angle-0.4), last.y - 8*Math.sin(angle-0.4));
                ctx.lineTo(last.x - 8*Math.cos(angle+0.4), last.y - 8*Math.sin(angle+0.4));
                ctx.closePath();
                ctx.fillStyle = 'rgba(255,200,87,0.7)';
                ctx.fill();
            }
        }
        var tirIdx = Math.floor(steps / 2);
        var tirPt = points[tirIdx];
        var tirAlpha = 0.3 + 0.2 * Math.sin(time * 3);
        ctx.beginPath();
        ctx.arc(tirPt.x, tirPt.y, 6, 0, Math.PI*2);
        ctx.fillStyle = 'rgba(255,34,68,' + tirAlpha + ')';
        ctx.fill();
        ctx.fillStyle = '#ff2244';
        ctx.font = 'bold 10px Cairo';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'alphabetic';
        ctx.fillText('TIR', tirPt.x, tirPt.y - 12);
    }

    function animate(){
        time += 0.016;
        ctx.clearRect(0, 0, W, H);
        drawScene();
        requestAnimationFrame(animate);
    }
    animate();

    window.addEventListener('resize', function(){
        W = window.innerWidth;
        H = window.innerHeight;
        if(W < 100) W = 700;
        if(H < 100) H = 440;
        cv.width = W;
        cv.height = H;
    });
});
</script>
</body></html>"""


# ============================================================
#  CONDITION FIGURES TEMPLATE (جديد - للشكل أ و ب)
# ============================================================
def get_condition_figure_html():
    return """<!DOCTYPE html>
<html dir="rtl"><head><meta charset="UTF-8">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:#070b14;font-family:'Cairo',Arial,sans-serif}
canvas{display:block;width:100%;height:100%}
.fig-title{position:absolute;top:8px;left:50%;transform:translateX(-50%);font-size:13px;font-weight:700;color:#e8ecf4;white-space:nowrap}
.fig-a{position:absolute;top:50%;left:25%;transform:translate(-50%,-50%);font-size:18px;font-weight:900;color:#ff4466}
.fig-b{position:absolute;top:50%;right:25%;transform:translate(50%,-50%);font-size:18px;font-weight:900;color:#00e5a0}
.result-a{position:absolute;bottom:52%;left:8%;font-size:11px;font-weight:700;color:#ff4466;white-space:nowrap;text-align:center}
.result-b{position:absolute;bottom:52%;right:8%;font-size:11px;font-weight:700;color:#00e5a0;white-space:nowrap;text-align:center}
</style></head><body>
<canvas id="cv"></canvas>
<div class="fig-a">\u0627\u0644\u0634\u0643\u0644 (\u0623)</div>
<div class="fig-b">\u0627\u0644\u0634\u0643\u0644 (\u0628)</div>
<div class="result-a">\u2717 \u0644\u0627 \u064A\u062D\u0642\u0642 \u0627\u0644\u0634\u0631\u0637<br>n\u2081 < n\u2082</div>
<div class="result-b">\u2713 \u064A\u062D\u0642\u0642 \u0627\u0644\u0634\u0631\u0637<br>n\u2081 > n\u2082</div>
<script>
window.addEventListener('load', function(){
    var cv = document.getElementById('cv');
    var ctx = cv.getContext('2d');
    var W = window.innerWidth;
    var H = window.innerHeight;
    if(W < 100) W = 800;
    if(H < 100) H = 350;
    cv.width = W;
    cv.height = H;

    function drawFigure(ox, oy, w, h, theta1Deg, theta2Deg, mode, n1, n2) {
        var boundary = oy + h * 0.42;
        var rayLen = Math.min(w, h) * 0.38;
        if(rayLen < 20) rayLen = 60;

        // Medium 1 (top) lighter
        ctx.fillStyle = 'rgba(40,50,70,0.06)';
        ctx.fillRect(ox, oy, w, boundary - oy);

        // Medium 2 (bottom) darker
        var mGrad = ctx.createLinearGradient(0, boundary, 0, oy + h);
        mGrad.addColorStop(0, 'rgba(30,100,180,0.15)');
        mGrad.addColorStop(1, 'rgba(20,70,140,0.08)');
        ctx.fillStyle = mGrad;
        ctx.fillRect(ox, boundary, w, oy + h - boundary);

        // Boundary line
        ctx.beginPath();
        ctx.moveTo(ox, boundary);
        ctx.lineTo(ox + w, boundary);
        ctx.strokeStyle = 'rgba(0,229,160,0.25)';
        ctx.lineWidth = 1;
        ctx.stroke();

        // Normal
        var ncx = ox + w * 0.5;
        ctx.beginPath();
        ctx.setLineDash([4,4]);
        ctx.moveTo(ncx, oy + 15);
        ctx.lineTo(ncx, oy + h - 10);
        ctx.strokeStyle = 'rgba(255,255,255,0.2)';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.setLineDash([]);

        // Normal label
        ctx.fillStyle = 'rgba(255,255,255,0.3)';
        ctx.font = '9px Cairo';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'alphabetic';
        ctx.fillText('N', ncx + 4, oy + 25);

        // Medium labels
        ctx.font = '10px Cairo';
        ctx.textAlign = 'center';
        if(mode === 'a'){
            ctx.fillStyle = 'rgba(150,170,200,0.4)';
            ctx.fillText('\u0647\u0648\u0627\u0621 (n\u2081=' + n1 + ')', ncx, oy + 15);
            ctx.fillStyle = 'rgba(0,184,255,0.5)';
            ctx.fillText('\u0632\u062C\u0627\u062C (n\u2082=' + n2 + ')', ncx, oy + h - 5);
        } else {
            ctx.fillStyle = 'rgba(0,184,255,0.5)';
            ctx.fillText('\u0632\u062C\u0627\u062C (n\u2081=' + n1 + ')', ncx, oy + 15);
            ctx.fillStyle = 'rgba(150,170,200,0.4)';
            ctx.fillText('\u0647\u0648\u0627\u0621 (n\u2082=' + n2 + ')', ncx, oy + h - 5);
        }

        // Incident ray (from top to center)
        var t1 = theta1Deg * Math.PI / 180;
        var incSX, incSY, incEX, incEY;

        if(mode === 'a') {
            // Light goes from air (top) to glass (bottom)
            incSX = ncx - Math.sin(t1) * rayLen;
            incSY = boundary - Math.cos(t1) * rayLen;
            incEX = ncx;
            incEY = boundary;
        } else {
            // Light goes from glass (bottom) to air (top)
            incSX = ncx - Math.sin(t1) * rayLen;
            incSY = boundary + Math.cos(t1) * rayLen;
            incEX = ncx;
            incEY = boundary;
        }

        // Draw incident ray
        ctx.beginPath();
        ctx.moveTo(incSX, incSY);
        ctx.lineTo(incEX, incEY);
        ctx.strokeStyle = '#ff2244';
        ctx.lineWidth = 2.5;
        ctx.stroke();
        ctx.strokeStyle = 'rgba(255,34,68,0.1)';
        ctx.lineWidth = 7;
        ctx.stroke();

        // Incident arrow
        var arrA = Math.atan2(incEY - incSY, incEX - incSX);
        ctx.beginPath();
        ctx.moveTo(incEX, incEY);
        ctx.lineTo(incEX - 9*Math.cos(arrA-0.35), incEY - 9*Math.sin(arrA-0.35));
        ctx.lineTo(incEX - 9*Math.cos(arrA+0.35), incEY - 9*Math.sin(arrA+0.35));
        ctx.closePath();
        ctx.fillStyle = '#ff2244';
        ctx.fill();

        // Incident angle arc
        ctx.beginPath();
        if(mode === 'a') {
            ctx.arc(ncx, boundary, 32, -Math.PI/2, -Math.PI/2 + t1, false);
        } else {
            ctx.arc(ncx, boundary, 32, Math.PI/2, Math.PI/2 + t1, false);
        }
        ctx.strokeStyle = '#ffc857';
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.fillStyle = '#ffc857';
        ctx.font = 'bold 10px Courier New';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        if(mode === 'a') {
            ctx.fillText('\u03B8\u2081=' + theta1Deg + '\u00B0', ncx + 42, boundary - 22);
        } else {
            ctx.fillText('\u03B8\u2081=' + theta1Deg + '\u00B0', ncx + 42, boundary + 24);
        }

        // Refracted ray
        var t2 = theta2Deg * Math.PI / 180;
        var refEX, refEY;
        var refColor = '#00b8ff';

        if(mode === 'a') {
            // Refracted into glass (approaching normal)
            refEX = ncx + Math.sin(t2) * rayLen;
            refEY = boundary + Math.cos(t2) * rayLen;
        } else {
            // Refracted into air (away from normal)
            refEX = ncx + Math.sin(t2) * rayLen;
            refEY = boundary - Math.cos(t2) * rayLen;
        }

        ctx.beginPath();
        ctx.moveTo(incEX, incEY);
        ctx.lineTo(refEX, refEY);
        ctx.strokeStyle = refColor;
        ctx.lineWidth = 2.5;
        ctx.stroke();
        ctx.strokeStyle = 'rgba(0,184,255,0.1)';
        ctx.lineWidth = 7;
        ctx.stroke();

        // Refracted arrow
        var rArrA = Math.atan2(refEY - incEY, refEX - incEX);
        ctx.beginPath();
        ctx.moveTo(refEX, refEY);
        ctx.lineTo(refEX - 9*Math.cos(rArrA-0.35), refEY - 9*Math.sin(rArrA-0.35));
        ctx.lineTo(refEX - 9*Math.cos(rArrA+0.35), refEY - 9*Math.sin(rArrA+0.35));
        ctx.closePath();
        ctx.fillStyle = refColor;
        ctx.fill();

        // Refraction angle arc
        ctx.beginPath();
        if(mode === 'a') {
            ctx.arc(ncx, boundary, 28, Math.PI/2, Math.PI/2 - t2, true);
        } else {
            ctx.arc(ncx, boundary, 28, -Math.PI/2, -Math.PI/2 - t2, true);
        }
        ctx.strokeStyle = refColor;
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.fillStyle = refColor;
        ctx.font = 'bold 10px Courier New';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        if(mode === 'a') {
            ctx.fillText('\u03B8\u2082=' + theta2Deg + '\u00B0', ncx - 42, boundary + 22);
        } else {
            ctx.fillText('\u03B8\u2082=' + theta2Deg + '\u00B0', ncx - 42, boundary - 22);
        }

        // Comparison note
        ctx.font = 'bold 10px Cairo';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'alphabetic';
        if(mode === 'a') {
            ctx.fillStyle = '#ff4466';
            ctx.fillText('\u03B8\u2081=' + theta1Deg + '\u00B0 < \u03B8\u2082=' + theta2Deg + '\u00B0  \u2192  n\u2081 < n\u2082', ncx, oy + h + 16);
        } else {
            ctx.fillStyle = '#00e5a0';
            ctx.fillText('\u03B8\u2081=' + theta1Deg + '\u00B0 > \u03B8\u2082=' + theta2Deg + '\u00B0  \u2192  n\u2081 > n\u2082', ncx, oy + h + 16);
        }

        // Hit point
        ctx.beginPath();
        ctx.arc(ncx, boundary, 3, 0, Math.PI*2);
        ctx.fillStyle = '#ffffff';
        ctx.fill();
    }

    // Draw Figure A (left half): air→glass, θ₁=37°, θ₂=55°
    var margin = 20;
    var halfW = (W - margin * 3) / 2;
    var figH = H * 0.7;
    var figY = H * 0.12;

    drawFigure(margin, figY, halfW, figH, 37, 55, 'a', 1.4, 1.8);
    drawFigure(margin * 2 + halfW, figY, halfW, figH, 55, 37, 'b', 1.8, 1.4);

    // Divider
    ctx.beginPath();
    ctx.moveTo(W/2, figY);
    ctx.lineTo(W/2, figY + figH + 20);
    ctx.strokeStyle = 'rgba(255,255,255,0.06)';
    ctx.lineWidth = 1;
    ctx.stroke();
});
</script></body></html>"""

# ============================================================
#  RAY PATH TEMPLATE (المصححة)
# ============================================================
def get_ray_path_html(case_num, angle, medium1, n1, n2):
    theta_c = calc_critical_angle(n1, n2)
    theta_c_str = f"{theta_c:.1f}" if theta_c else "N/A"

    if theta_c and angle < theta_c - 0.5:
        mode = "refraction"
        theta2 = calc_refraction_angle(n1, angle, n2)
        theta2_str = f"{theta2:.1f}" if theta2 else "N/A"
    elif theta_c and abs(angle - theta_c) <= 0.5:
        mode = "critical"
        theta2_str = "90.0"
    else:
        mode = "reflection"
        theta2_str = "N/A"

    if mode == "refraction":
        badge_class = "badge-ref"
        badge_css = "background:rgba(0,184,255,0.15);border:1px solid rgba(0,184,255,0.4);color:#00b8ff"
        mode_text = "\u0627\u0646\u0643\u0633\u0627\u0631 \u0645\u0628\u062A\u0639\u062F \u0639\u0646 \u0627\u0644\u0639\u0645\u0648\u062F"
    elif mode == "critical":
        badge_class = "badge-crit"
        badge_css = "background:rgba(255,200,87,0.15);border:1px solid rgba(255,200,87,0.4);color:#ffc857"
        mode_text = "\u0627\u0644\u0632\u0627\u0648\u064A\u0629 \u0627\u0644\u062D\u0631\u062C\u0629 (\u03B8\u2082 = 90\u00B0)"
    else:
        badge_class = "badge-tir"
        badge_css = "background:rgba(255,34,68,0.15);border:1px solid rgba(255,34,68,0.4);color:#ff2244"
        mode_text = "\u0627\u0646\u0639\u0643\u0627\u0633 \u0643\u0644\u064A \u062F\u0627\u062E\u0644\u064A"

    return """<!DOCTYPE html>
<html dir="rtl"><head><meta charset="UTF-8">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:#070b14;font-family:'Cairo',Arial,sans-serif}
canvas{display:block;width:100%;height:100%}
.case-label{position:absolute;top:8px;right:12px;background:rgba(13,21,37,0.9);border:1px solid #1a2744;border-radius:8px;padding:6px 14px;color:#a0b0c8;font-size:12px;direction:rtl}
.case-label .v{color:#00e5a0;font-weight:700;direction:ltr;display:inline-block}
.mode-badge{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);padding:6px 18px;border-radius:8px;font-size:12px;font-weight:700;white-space:nowrap;""" + badge_css + """}
</style></head><body>
<canvas id="cv"></canvas>
<div class="case-label">
\u0632\u0627\u0648\u064A\u0629 \u0627\u0644\u0633\u0642\u0648\u0637: <span class="v">""" + str(angle) + """\u00B0</span> |
\u03B8c = <span class="v">""" + theta_c_str + """\u00B0</span> |
n\u2081 = <span class="v">""" + str(n1) + """</span> | n\u2082 = <span class="v">""" + str(n2) + """</span>
</div>
<div class="mode-badge">""" + mode_text + """</div>
<script>
window.addEventListener('load', function(){
    var cv = document.getElementById('cv');
    var ctx = cv.getContext('2d');
    var W = window.innerWidth;
    var H = window.innerHeight;
    if(W < 100) W = 600;
    if(H < 100) H = 320;
    cv.width = W;
    cv.height = H;

    var ANGLE = """ + str(angle) + """;
    var N1 = """ + str(n1) + """;
    var N2 = """ + str(n2) + """;
    var MODE = '""" + mode + """';
    var THETA2 = """ + theta2_str + """;
    var MEDIUM1 = '""" + medium1 + """';

    var cx = W * 0.5;
    var boundary = H * 0.45;
    var rayLen = Math.min(W, H) * 0.35;
    if(rayLen < 30) rayLen = 100;

    var m1G = ctx.createLinearGradient(0, boundary, 0, H);
    m1G.addColorStop(0, 'rgba(30,100,180,0.15)');
    m1G.addColorStop(1, 'rgba(20,70,140,0.08)');
    ctx.fillStyle = m1G;
    ctx.fillRect(0, boundary, W, H - boundary);
    ctx.strokeStyle = 'rgba(30,100,180,0.3)';
    ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(0, boundary); ctx.lineTo(W, boundary); ctx.stroke();

    ctx.fillStyle = 'rgba(40,50,70,0.05)';
    ctx.fillRect(0, 0, W, boundary);

    ctx.fillStyle = 'rgba(0,184,255,0.5)';
    ctx.font = 'bold 12px Cairo';
    ctx.textAlign = 'left';
    ctx.textBaseline = 'alphabetic';
    ctx.fillText(MEDIUM1 + ' (n\\u2081=' + N1 + ')', 12, boundary + 22);
    ctx.fillStyle = 'rgba(150,170,200,0.4)';
    ctx.fillText('\\u0647\\u0648\\u0627\\u0621 (n\\u2082=' + N2 + ')', 12, boundary - 10);

    ctx.beginPath();
    ctx.setLineDash([5,5]);
    ctx.moveTo(cx, boundary - rayLen - 20);
    ctx.lineTo(cx, boundary + rayLen + 20);
    ctx.strokeStyle = 'rgba(255,255,255,0.2)';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = 'rgba(255,255,255,0.3)';
    ctx.font = '10px Cairo';
    ctx.textAlign = 'left';
    ctx.fillText('N', cx + 5, boundary - rayLen - 8);

    var aRad = ANGLE * Math.PI / 180;
    var incSX = cx - Math.sin(aRad) * rayLen;
    var incSY = boundary + Math.cos(aRad) * rayLen;

    ctx.beginPath();
    ctx.moveTo(incSX, incSY);
    ctx.lineTo(cx, boundary);
    ctx.strokeStyle = '#ff2244';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    ctx.strokeStyle = 'rgba(255,34,68,0.1)';
    ctx.lineWidth = 8;
    ctx.stroke();

    var arrA = Math.atan2(boundary - incSY, cx - incSX);
    ctx.beginPath();
    ctx.moveTo(cx, boundary);
    ctx.lineTo(cx - 10*Math.cos(arrA-0.35), boundary - 10*Math.sin(arrA-0.35));
    ctx.lineTo(cx - 10*Math.cos(arrA+0.35), boundary - 10*Math.sin(arrA+0.35));
    ctx.closePath();
    ctx.fillStyle = '#ff2244';
    ctx.fill();

    ctx.beginPath();
    ctx.arc(cx, boundary, 40, Math.PI/2, Math.PI/2 + aRad, true);
    ctx.strokeStyle = '#ffc857';
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.fillStyle = '#ffc857';
    ctx.font = 'bold 11px Courier New';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('\\u03B8\\u2081=' + ANGLE + '\\u00B0', cx - 58, boundary + 32);

    if(MODE === 'refraction') {
        var t2 = parseFloat(THETA2) * Math.PI / 180;
        var refEX = cx + Math.sin(t2) * rayLen;
        var refEY = boundary - Math.cos(t2) * rayLen;
        ctx.beginPath(); ctx.moveTo(cx, boundary); ctx.lineTo(refEX, refEY);
        ctx.strokeStyle = '#00b8ff'; ctx.lineWidth = 2.5; ctx.stroke();
        ctx.strokeStyle = 'rgba(0,184,255,0.1)'; ctx.lineWidth = 8; ctx.stroke();
        var rA = Math.atan2(refEY - boundary, refEX - cx);
        ctx.beginPath();
        ctx.moveTo(refEX, refEY);
        ctx.lineTo(refEX - 10*Math.cos(rA-0.35), refEY - 10*Math.sin(rA-0.35));
        ctx.lineTo(refEX - 10*Math.cos(rA+0.35), refEY - 10*Math.sin(rA+0.35));
        ctx.closePath(); ctx.fillStyle = '#00b8ff'; ctx.fill();
        ctx.beginPath();
        ctx.arc(cx, boundary, 35, -Math.PI/2, -Math.PI/2 + t2, false);
        ctx.strokeStyle = '#00b8ff'; ctx.lineWidth = 1.5; ctx.stroke();
        ctx.fillStyle = '#00b8ff'; ctx.font = 'bold 11px Courier New';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('\\u03B8\\u2082=' + THETA2 + '\\u00B0', cx + 58, boundary - 28);
    } else if(MODE === 'critical') {
        var crEX = cx + rayLen;
        ctx.beginPath(); ctx.moveTo(cx, boundary); ctx.lineTo(crEX, boundary);
        ctx.strokeStyle = '#ffc857'; ctx.lineWidth = 2.5; ctx.stroke();
        ctx.strokeStyle = 'rgba(255,200,87,0.1)'; ctx.lineWidth = 8; ctx.stroke();
        ctx.fillStyle = '#ffc857'; ctx.font = 'bold 11px Courier New';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText('\\u03B8\\u2082 = 90\\u00B0', cx + rayLen/2, boundary - 12);
    } else {
        var rlEX = cx + Math.sin(aRad) * rayLen;
        var rlEY = boundary + Math.cos(aRad) * rayLen;
        ctx.beginPath(); ctx.moveTo(cx, boundary); ctx.lineTo(rlEX, rlEY);
        ctx.strokeStyle = '#ff2244'; ctx.lineWidth = 2.5; ctx.stroke();
        ctx.strokeStyle = 'rgba(255,34,68,0.1)'; ctx.lineWidth = 8; ctx.stroke();
        var rA2 = Math.atan2(rlEY - boundary, rlEX - cx);
        ctx.beginPath();
        ctx.moveTo(rlEX, rlEY);
        ctx.lineTo(rlEX - 10*Math.cos(rA2-0.35), rlEY - 10*Math.sin(rA2-0.35));
        ctx.lineTo(rlEX - 10*Math.cos(rA2+0.35), rlEY - 10*Math.sin(rA2+0.35));
        ctx.closePath(); ctx.fillStyle = '#ff2244'; ctx.fill();
        ctx.beginPath();
        ctx.arc(cx, boundary, 35, Math.PI/2 - aRad, Math.PI/2, false);
        ctx.strokeStyle = '#ff6688'; ctx.lineWidth = 1.5; ctx.stroke();
        ctx.fillStyle = '#ff6688'; ctx.font = 'bold 11px Courier New';
        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillText("\\u03B8'=" + ANGLE + '\\u00B0', cx + 58, boundary + 32);
    }

    ctx.beginPath(); ctx.arc(cx, boundary, 4, 0, Math.PI*2);
    ctx.fillStyle = '#ffffff'; ctx.fill();
});
</script></body></html>"""


# ============================================================
#  EXPERIMENT TEMPLATE (المصححة)
# ============================================================
def get_experiment_html():
    return """<!DOCTYPE html>
<html dir="rtl"><head><meta charset="UTF-8">
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:100%;height:100%;overflow:hidden;background:#070b14;font-family:'Cairo',Arial,sans-serif}
canvas{display:block;width:100%;height:100%}
</style></head><body>
<canvas id="cv"></canvas>
<script>
window.addEventListener('load', function(){
    var cv = document.getElementById('cv');
    var ctx = cv.getContext('2d');
    var W = window.innerWidth;
    var H = window.innerHeight;
    if(W < 100) W = 700;
    if(H < 100) H = 380;
    cv.width = W;
    cv.height = H;

    var cx = W * 0.5;
    var cy = H * 0.5;
    var R = Math.min(W, H) * 0.35;
    if(R < 50) R = 120;

    ctx.beginPath();
    ctx.arc(cx, cy, R, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(0,229,160,0.2)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    for(var i=0; i<360; i+=10){
        var a = i * Math.PI / 180;
        var inner = (i%30 === 0) ? R - 15 : R - 8;
        ctx.beginPath();
        ctx.moveTo(cx + Math.cos(a)*inner, cy - Math.sin(a)*inner);
        ctx.lineTo(cx + Math.cos(a)*R, cy - Math.sin(a)*R);
        ctx.strokeStyle = 'rgba(0,229,160,0.08)';
        ctx.lineWidth = 1;
        ctx.stroke();
        if(i % 30 === 0){
            ctx.fillStyle = 'rgba(0,229,160,0.35)';
            ctx.font = '9px Courier New';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(i+'', cx + Math.cos(a)*(R+14), cy - Math.sin(a)*(R+14));
        }
    }

    ctx.beginPath();
    ctx.arc(cx, cy, R * 0.85, 0, Math.PI);
    ctx.closePath();
    var gGrad = ctx.createLinearGradient(cx, cy, cx, cy + R*0.85);
    gGrad.addColorStop(0, 'rgba(60,140,220,0.12)');
    gGrad.addColorStop(1, 'rgba(40,100,180,0.06)');
    ctx.fillStyle = gGrad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(60,140,220,0.35)';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(cx - R*0.85, cy);
    ctx.lineTo(cx + R*0.85, cy);
    ctx.strokeStyle = 'rgba(60,140,220,0.5)';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.beginPath();
    ctx.setLineDash([4,4]);
    ctx.moveTo(cx, cy - R - 10);
    ctx.lineTo(cx, cy + R*0.85 + 10);
    ctx.strokeStyle = 'rgba(255,255,255,0.25)';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.setLineDash([]);

    ctx.fillStyle = '#00e5a0';
    ctx.font = 'bold 13px Cairo';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'top';
    ctx.fillText('\u0627\u0644\u062A\u062C\u0631\u0628\u0629: \u0627\u0644\u0627\u0646\u0639\u0643\u0627\u0633 \u0627\u0644\u0643\u0644\u064A \u0627\u0644\u062F\u0627\u062E\u0644\u064A', cx, 8);

    ctx.fillStyle = 'rgba(60,140,220,0.5)';
    ctx.font = '11px Cairo';
    ctx.textBaseline = 'middle';
    ctx.fillText('\u0642\u0631\u0635 \u0632\u062C\u0627\u062C\u064A \u0646\u0635\u0641 \u062F\u0627\u0626\u0631\u064A (n=1.50)', cx, cy + R*0.5);

    ctx.fillStyle = 'rgba(255,255,255,0.3)';
    ctx.font = '10px Cairo';
    ctx.textAlign = 'left';
    ctx.fillText('N', cx + 6, cy - R - 5);

    var theta = 55 * Math.PI / 180;
    var rStartX = cx + Math.sin(theta) * R * 0.7;
    var rStartY = cy + Math.cos(theta) * R * 0.7;

    ctx.beginPath();
    ctx.moveTo(rStartX, rStartY);
    ctx.lineTo(cx, cy);
    ctx.strokeStyle = '#ff2244';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    ctx.strokeStyle = 'rgba(255,34,68,0.1)';
    ctx.lineWidth = 7;
    ctx.stroke();

    var rlEndX = cx - Math.sin(theta) * R * 0.7;
    var rlEndY = cy + Math.cos(theta) * R * 0.7;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(rlEndX, rlEndY);
    ctx.strokeStyle = '#ff2244';
    ctx.lineWidth = 2.5;
    ctx.stroke();
    ctx.strokeStyle = 'rgba(255,34,68,0.1)';
    ctx.lineWidth = 7;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(cx, cy, 38, Math.PI/2 - theta, Math.PI/2, false);
    ctx.strokeStyle = '#ffc857';
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.fillStyle = '#ffc857';
    ctx.font = 'bold 11px Courier New';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('55\u00B0', cx - 50, cy + 20);

    ctx.beginPath();
    ctx.arc(cx, cy, 33, Math.PI/2, Math.PI/2 + theta, false);
    ctx.strokeStyle = '#ff6688';
    ctx.lineWidth = 1.5;
    ctx.stroke();
    ctx.fillStyle = '#ff6688';
    ctx.fillText("55\u00B0", cx + 45, cy + 20);

    ctx.fillStyle = '#ff2244';
    ctx.font = 'bold 13px Cairo';
    ctx.fillText('TIR (\u03B8\u2081 > \u03B8c)', cx, cy - 30);

    ctx.fillStyle = 'rgba(255,255,255,0.15)';
    ctx.font = '10px Cairo';
    ctx.textAlign = 'center';
    ctx.fillText('\u0635\u0646\u062F\u0648\u0642 \u0636\u0648\u0626\u064A', rStartX + 20, rStartY - 10);

    ctx.beginPath();
    ctx.arc(cx, cy, 4, 0, Math.PI*2);
    ctx.fillStyle = '#ffffff';
    ctx.fill();

    ctx.fillStyle = 'rgba(150,170,200,0.4)';
    ctx.font = '10px Cairo';
    ctx.textAlign = 'right';
    ctx.fillText('\u0647\u0648\u0627\u0621 (n=1.00)', cx - R*0.85 - 8, cy - 15);
});
</script></body></html>"""


# ============================================================
#  MAIN APPLICATION
# ============================================================
def main():
    # ---- HEADER ----
    st.markdown("""
    <div class="main-header">
        <div class="header-title">الانعكاس الكلي الداخلي والزاوية الحرجة</div>
        <div class="header-sub">Total Internal Reflection & Critical Angle</div>
        <div class="author-badge">إعداد: Israa Youssuf Samara &nbsp;|&nbsp; فيزياء: الصف التاسع</div>
    </div>
    """, unsafe_allow_html=True)

    # ---- TABS ----
    tabs = st.tabs([
        "🔬 المحاكاة التفاعلية",
        "📐 حساب الزاوية الحرجة",
        "🧪 التجربة العملية",
        "📝 أمثلة تفاعلية",
        "🌈 ظواهر ضوئية",
        "✅ تقويم الدرس"
    ])

    # ========================================================
    #  TAB 1: INTERACTIVE 3D SIMULATION
    # ========================================================
    with tabs[0]:
        st.markdown('<div class="section-title"><span class="icon">🔬</span> المحاكاة التفاعلية ثلاثية الأبعاد</div>', unsafe_allow_html=True)

        col_ctrl, col_sim = st.columns([1, 3])

        with col_ctrl:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("#### إعدادات المحاكاة")

            medium_choice = st.selectbox(
                "الوسط الأول (الأكثف)",
                ["زجاج (n = 1.50)", "ماء (n = 1.33)", "ماس (n = 2.42)", "مخصص"],
                key="sim_medium"
            )

            n1_map = {
                "زجاج (n = 1.50)": 1.50,
                "ماء (n = 1.33)": 1.33,
                "ماس (n = 2.42)": 2.42,
                "مخصص": 1.50
            }
            n1_val = n1_map[medium_choice]

            if medium_choice == "مخصص":
                n1_val = st.number_input("n₁", min_value=1.01, max_value=3.0, value=1.50, step=0.01, key="n1_custom")

            n2_val = st.number_input("n₂ (الوسط الأقل كثافة)", min_value=1.00, max_value=2.99, value=1.00, step=0.01)

            angle_val = st.slider(
                "زاوية السقوط θ₁ (°)",
                min_value=0.0, max_value=89.0, value=30.0, step=0.5,
                key="angle_slider"
            )

            theta_c = calc_critical_angle(n1_val, n2_val)

            st.markdown("---")
            st.markdown("#### النتائج")

            if theta_c is not None:
                st.markdown(f'<div class="formula-box">θc = {theta_c:.1f}°</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="formula-box" style="border-color:rgba(255,34,68,0.4);background:rgba(255,34,68,0.08);">لا يمكن حدوث TIR (n₁ ≤ n₂)</div>', unsafe_allow_html=True)

            theta2 = calc_refraction_angle(n1_val, angle_val, n2_val)

            if theta_c is not None:
                if angle_val < theta_c - 0.3:
                    st.markdown(f'<span class="result-badge badge-refraction">انكسار: θ₂ = {theta2:.1f}°</span>', unsafe_allow_html=True)
                elif angle_val > theta_c + 0.3:
                    st.markdown('<span class="result-badge badge-tir">انعكاس كلي داخلي TIR</span>', unsafe_allow_html=True)
                else:
                    st.markdown('<span class="result-badge badge-critical">الزاوية الحرجة: θ₂ = 90°</span>', unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("#### الشرح")
            if theta_c is not None:
                if angle_val < theta_c - 0.3:
                    st.info(f"θ₁ = {angle_val:.1f}° < θc = {theta_c:.1f}° → ينكسر الشعاع مبتعدًا عن العمود في الوسط الأقل كثافة")
                elif angle_val > theta_c + 0.3:
                    st.error(f"θ₁ = {angle_val:.1f}° > θc = {theta_c:.1f}° → ينعكس الشعاع انعكاسًا كليًّا داخليًّا، θ₁' = θ₁ = {angle_val:.1f}°")
                else:
                    st.warning(f"θ₁ = {angle_val:.1f}° ≈ θc = {theta_c:.1f}° → الشعاع المنكسر يصبح ملامسًا للحد الفاصل (θ₂ = 90°)")

            st.markdown('</div>', unsafe_allow_html=True)

        with col_sim:
            html = get_tir_3d_html(angle_val, n1_val, n2_val)
            components.html(html, height=530)

        # Explanation section
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### القوانين والشروط")
        st.markdown('<div class="formula-box">n₁ sin θ₁ = n₂ sin θ₂ &nbsp;&nbsp; (Snell\'s Law)</div>', unsafe_allow_html=True)
        st.markdown('<div class="formula-box">sin θc = n₂ / n₁</div>', unsafe_allow_html=True)
        if n2_val == 1.0:
            st.markdown('<div class="formula-box">sin θc = 1 / n₁</div>', unsafe_allow_html=True)

        st.markdown('<div class="condition-box">', unsafe_allow_html=True)
        st.markdown('<div class="cond-title">شروط حدوث الانعكاس الكلي الداخلي:</div>')
        st.markdown("""<ul>
            <li>ينتقل الضوء من وسط شفاف إلى وسط شفاف آخر معامل انكساره أقل (n₁ > n₂)</li>
            <li>تكون زاوية السقوط أكبر من الزاوية الحرجة (θ₁ > θc)</li>
            <li>زاوية السقوط مساوية لزاوية الانعكاس (θ₁ = θ₁')</li>
        </ul>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    #  TAB 2: CRITICAL ANGLE CALCULATION
    # ========================================================
    with tabs[1]:
        st.markdown('<div class="section-title"><span class="icon">📐</span> حساب الزاوية الحرجة لأوساط شفافة</div>', unsafe_allow_html=True)

        st.markdown('<div class="formula-box">sin θc = n₂ / n₁ &nbsp;&nbsp;|&nbsp;&nbsp; sin θc = 1 / n &nbsp;(إذا كان الوسط الثاني هو الهواء)</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### أمثلة محلولة")
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        examples_calc = [
            {"name": "الماء", "n": 1.33, "n2": 1.0},
            {"name": "الزجاج", "n": 1.50, "n2": 1.0},
            {"name": "الماس", "n": 2.42, "n2": 1.0},
            {"name": "الزجاج → ماء", "n": 1.50, "n2": 1.33},
            {"name": "الماس → زجاج", "n": 2.42, "n2": 1.50},
        ]

        for ex in examples_calc:
            tc = calc_critical_angle(ex["n"], ex["n2"])
            if tc:
                formula = f"sin θc = {ex['n2']} / {ex['n']} = {ex['n2']/ex['n']:.4f}"
                result = f"θc = {tc:.1f}°"
            else:
                formula = "لا يمكن (n₁ ≤ n₂)"
                result = "—"

            col_name, col_f, col_r = st.columns([1.5, 2.5, 1])
            with col_name:
                st.markdown(f"**{ex['name']}**")
                st.markdown(f"<span style='color:#7a8ba8;font-size:0.8rem'>n₁ = {ex['n']}, n₂ = {ex['n2']}</span>", unsafe_allow_html=True)
            with col_f:
                st.code(formula, language="text")
            with col_r:
                st.markdown(f"<span style='color:#00e5a0;font-size:1.2rem;font-weight:700'>{result}</span>", unsafe_allow_html=True)
            st.markdown("<div style='border-bottom:1px solid rgba(255,255,255,0.05);margin:4px 0'></div>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### جرب بنفسك — آلة حاسبة للزاوية الحرجة")
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)

        c2a, c2b, c2c = st.columns(3)
        with c2a:
            calc_medium = st.selectbox(
                "اختر الوسط",
                ["زجاج", "ماء", "ماس", "كوارتز (n=1.46)", "مخصص"],
                key="calc_medium_sel"
            )
        with c2b:
            n_map = {"زجاج": 1.50, "ماء": 1.33, "ماس": 2.42, "كوارتز (n=1.46)": 1.46, "مخصص": 1.50}
            n1_input = n_map[calc_medium]
            if calc_medium == "مخصص":
                n1_input = st.number_input("n₁", min_value=1.01, max_value=4.0, value=1.50, step=0.01, key="calc_n1")
        with c2c:
            n2_input = st.number_input("n₂", min_value=1.00, max_value=3.99, value=1.00, step=0.01, key="calc_n2")

        tc_result = calc_critical_angle(n1_input, n2_input)

        if tc_result is not None:
            sin_val = n2_input / n1_input
            st.markdown(f"""
            <div style='background:rgba(0,229,160,0.06);border:1px solid rgba(0,229,160,0.2);border-radius:12px;padding:16px 24px;margin-top:12px;direction:ltr;text-align:center'>
                <div style='color:#7a8ba8;font-size:0.85rem;margin-bottom:6px'>Snell's Law at Critical Angle</div>
                <div style='font-size:1.1rem;color:#fff;font-family:Courier New,monospace'>
                    sin θc = n₂ / n₁ = {n2_input} / {n1_input} = {sin_val:.4f}
                </div>
                <div style='font-size:1.6rem;color:#00e5a0;font-weight:900;margin-top:8px'>
                    θc = {tc_result:.1f}°
                </div>
            </div>
            """, unsafe_allow_html=True)

            vis_html = get_ray_path_html(0, tc_result, calc_medium, n1_input, n2_input)
            components.html(vis_html, height=330)
        else:
            st.error("لا يمكن حساب الزاوية الحرجة لأن n₁ ≤ n₂. يجب أن ينتقل الضوء من وسط أكثف إلى أقل كثافة.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    #  TAB 3: EXPERIMENT
    # ========================================================
    with tabs[2]:
        st.markdown('<div class="section-title"><span class="icon">🧪</span> التجربة العملية: الانعكاس الكلي الداخلي</div>', unsafe_allow_html=True)

        exp_html = get_experiment_html()
        components.html(exp_html, height=390)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📋 المواد والأدوات")
        st.markdown("""<ul style='list-style:none;padding:0'>
            <li style='padding:4px 0;color:#e8ecf4'>◆ صندوق ضوئي (مصدر شعاع ليزر ضيق)</li>
            <li style='padding:4px 0;color:#e8ecf4'>◆ قرص زجاجي نصف دائري (معامل انكساره معلوم، مثلاً n = 1.50)</li>
            <li style='padding:4px 0;color:#e8ecf4'>◆ منقلة دائرية</li>
            <li style='padding:4px 0;color:#e8ecf4'>◆ ورقة بيضاء A4 وقلم</li>
        </ul>""", unsafe_allow_html=True)

        st.markdown("#### ⚠️ إرشادات السلامة")
        st.markdown("<span style='color:#ffc857'>الحذر من سقوط الأجسام والأدوات على القدمين. عدم النظر مباشرة إلى الشعاع الضوئي.</span>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 📝 خطوات العمل")

        steps = [
            "أثبّت المنقلة الدائرية فوق الطاولة، ثم أضع ورقة بيضاء على سطحها.",
            "أضع القرص الزجاجي عند منتصف المنقلة على أن ينطبق مركز القرص على مركز المنقلة.",
            "أعلّم بالقلم حول القرص الدائري، ثم أنشئ بالقلم عمودًا على الوجه المستوي للقرص من مركزه.",
            "أسقط حزمة ضوئية ضيقة من الصندوق الضوئي على الوجه المستوي من القرص، على أن تكون موازية لسطح الورقة وتصنع زاوية مع العمود المرسوم، ثم أقيس زاويتي السقوط والانكسار.",
            "أزيد من زاوية سقوط الشعاع تدريجيًّا حتى أصل إلى أكبر زاوية سقوط ممكنة عندما يكون الشعاع الساقط محاذيًا للوجه المستوي، وألاحظ تغيّر زاوية الانكسار.",
            "أغيّر الجهة التي تسقط فيها الحزمة الضوئية على الوجه الدائري، مُراعيًا سقوطها بزاوية تجعل الشعاع يخرج من الجهة المقابلة (مثلاً 30°)، ثم أقيس زاوية الانكسار.",
            "أزيد من زاوية السقوط تدريجيًّا حتى يخرج الشعاع ملامسًا للوجه المستوي من القرص، وأقيس زاوية السقوط (هذه هي الزاوية الحرجة).",
            "أزيد زاوية السقوط عن الزاوية الحرجة، وألاحظ مسار الحزمة الضوئية، ثم أقيس الزاوية التي تصنعها مع العمود."
        ]

        for i, step in enumerate(steps, 1):
            st.markdown(f"""<div class="exp-step">
                <span class="exp-step-num">{i}</span>
                <span style='font-size:0.9rem;color:#e8ecf4'>{step}</span>
            </div>""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### 🔍 الملاحظة والاستنتاج")

        st.markdown("""
        <div style='margin-bottom:12px'>
            <span style='color:#ffc857;font-weight:700'>الملاحظة:</span>
            <span style='color:#e8ecf4;font-size:0.9rem'>
            عند انتقال الضوء من الزجاج إلى الهواء: كلما زادت زاوية السقوط زادت زاوية الانكسار.
            وعند زاوية سقوط معيّنة (الزاوية الحرجة ≈ 41.8° للزجاج) يصبح الشعاع المنكسر ملامسًا للحد الفاصل.
            وما زاد عنها ينعكس الشعاع كليًّا داخل الزجاج.
            </span>
        </div>
        <div style='margin-bottom:12px'>
            <span style='color:#00e5a0;font-weight:700'>الاستنتاج:</span>
            <span style='color:#e8ecf4;font-size:0.9rem'>
            لا يمكن حدوث الانعكاس الكلي الداخلي عند انتقال الضوء من الهواء إلى الزجاج (لأن n₁ < n₂).
            يحدث الانعكاس الكلي الداخلي فقط عند انتقال الضوء من وسط أكثف إلى أقل كثافة وبزاوية سقوط أكبر من الزاوية الحرجة.
            </span>
        </div>
        <div>
            <span style='color:#ff2244;font-weight:700'>شروط حدوث الانعكاس الكلي الداخلي:</span>
            <span style='color:#e8ecf4;font-size:0.9rem'>
            (1) n₁ > n₂ &nbsp;&nbsp; (2) θ₁ > θc &nbsp;&nbsp; (3) θ₁ = θ₁'
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    #  TAB 4: INTERACTIVE EXAMPLES
    # ========================================================
    with tabs[3]:
        st.markdown('<div class="section-title"><span class="icon">📝</span> أمثلة تفاعلية</div>', unsafe_allow_html=True)

        # --- Example Type 1 ---
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### النوع الأول: هل يحقق الشكل شرط حدوث الانعكاس الكلي الداخلي؟")

        # Draw figures A and B
        cond_fig_html = get_condition_figure_html()
        components.html(cond_fig_html, height=340)

        st.markdown("""
        <div style='background:rgba(255,200,87,0.06);border:1px solid rgba(255,200,87,0.2);border-radius:10px;padding:14px 18px;margin:10px 0;font-size:0.9rem;color:#e8ecf4'>
        <b style='color:#ffc857'>القاعدة:</b> إذا كانت θ₁ < θ₂ فإن n₁ > n₂ (حسب قانون سنل)، وهذا شرط ضروري لحدوث TIR.
        أما إذا كانت θ₁ > θ₂ فإن n₁ < n₂ ولا يمكن حدوث TIR.
        </div>
        """, unsafe_allow_html=True)

        tir_questions = [
            {"desc": "الشكل (أ): θ₁ = 37° , θ₂ = 55°", "theta1": 37, "theta2": 55, "n1": 1.8, "n2": 1.4},
            {"desc": "الشكل (ب): θ₁ = 55° , θ₂ = 37°", "theta1": 55, "theta2": 37, "n1": 1.8, "n2": 1.4},
        ]

        for q in tir_questions:
            can_tir = q["theta1"] < q["theta2"] and q["n1"] > q["n2"]
            st.markdown(f"**{q['desc']}**")
            if can_tir:
                tc = calc_critical_angle(q["n1"], q["n2"])
                st.markdown(f"""
                <div style='background:rgba(0,229,160,0.08);border:1px solid rgba(0,229,160,0.3);border-radius:8px;padding:10px 16px;margin:6px 0'>
                    <span style='color:#00e5a0;font-weight:700'>✓ يحقق الشرط</span> — لأن θ₁ < θ₂ يدل على n₁ > n₂.
                    الزاوية الحرجة θc = {tc:.1f}°. يجب أن θ₁ > {tc:.1f}° لحدوث TIR.
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style='background:rgba(255,34,68,0.08);border:1px solid rgba(255,34,68,0.3);border-radius:8px;padding:10px 16px;margin:6px 0'>
                    <span style='color:#ff2244;font-weight:700'>✗ لا يحقق الشرط</span> — لأن θ₁ > θ₂ يدل على n₁ < n₂، أي الضوء ينتقل من أقل كثافة إلى أكثف.
                </div>
                """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("**جرب بنفسك:**")
        ec1, ec2, ec3 = st.columns(3)
        with ec1:
            u_theta1 = st.number_input("θ₁ (°)", min_value=0.0, max_value=90.0, value=55.0, step=1.0, key="u_t1")
        with ec2:
            u_theta2 = st.number_input("θ₂ (°)", min_value=0.0, max_value=90.0, value=37.0, step=1.0, key="u_t2")
        with ec3:
            st.markdown("<br>", unsafe_allow_html=True)
            if u_theta1 < u_theta2 and u_theta1 != u_theta2:
                st.markdown("<span class='result-badge badge-tir'>✓ يحقق شرط n₁ > n₂</span>", unsafe_allow_html=True)
            elif u_theta1 == u_theta2:
                st.markdown("<span class='result-badge badge-critical'>n₁ = n₂ (لا انكسار)</span>", unsafe_allow_html=True)
            else:
                st.markdown("<span class='result-badge badge-refraction'>✗ لا يحقق (n₁ < n₂)</span>", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # --- Example Type 2 ---
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### النوع الثاني: حساب الزاوية الحرجة")

        st.markdown("**مثال 6:** إذا كان معاملَا الانكسار للوسطين الأول والثاني: n₁ = 1.8 , n₂ = 1.3 ، فأحسب الزاوية الحرجة.")
        st.code("sin θc = n₂ / n₁ = 1.3 / 1.8 = 0.722\nθc = arcsin(0.722) = 46.2°", language="text")

        st.markdown("**مثال 5:** أحسب الزاوية الحرجة للماء (n = 1.33).")
        st.code("sin θc = 1 / n = 1 / 1.33 = 0.7519\nθc = arcsin(0.7519) = 48.6°", language="text")

        st.markdown("---")
        st.markdown("**تمرين تفاعلي:**")
        tc1, tc2, tc3 = st.columns(3)
        with tc1:
            tc_n1 = st.number_input("n₁", min_value=1.01, max_value=4.0, value=1.50, step=0.01, key="tc_n1")
        with tc2:
            tc_n2 = st.number_input("n₂", min_value=1.00, max_value=3.99, value=1.00, step=0.01, key="tc_n2")
        with tc3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("احسب θc", key="calc_tc_btn"):
                result_tc = calc_critical_angle(tc_n1, tc_n2)
                if result_tc:
                    st.success(f"θc = {result_tc:.1f}°")
                else:
                    st.error("لا يمكن (n₁ ≤ n₂)")

        st.markdown('</div>', unsafe_allow_html=True)

        # --- Example Type 3 ---
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("#### النوع الثالث: إكمال مسارات الأشعة")
        st.markdown("<span style='color:#7a8ba8;font-size:0.85rem'>الزاوية الحرجة للماء = 48.6° (من المثال 5) — n₁ = 1.33 (ماء) , n₂ = 1.00 (هواء)</span>", unsafe_allow_html=True)

        ray_cases = [
            {"label": "الشكل (أ): θ₁ = 30° < θc → انكسار مبتعد عن العمود", "angle": 30, "medium": "ماء", "n1": 1.33, "n2": 1.0},
            {"label": "الشكل (ب): θ₁ = 48.6° = θc → الشعاع ملامس للحد الفاصل", "angle": 48.6, "medium": "ماء", "n1": 1.33, "n2": 1.0},
            {"label": "الشكل (جـ): θ₁ = 50° > θc → انعكاس كلي داخلي", "angle": 50, "medium": "ماء", "n1": 1.33, "n2": 1.0},
        ]

        for i, case in enumerate(ray_cases):
            st.markdown(f"**{case['label']}**")
            vis = get_ray_path_html(i, case["angle"], case["medium"], case["n1"], case["n2"])
            components.html(vis, height=330)

        st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    #  TAB 5: PHENOMENA
    # ========================================================
    with tabs[4]:
        st.markdown('<div class="section-title"><span class="icon">🌈</span> ظواهر على انكسار الضوء والانعكاس الكلي الداخلي</div>', unsafe_allow_html=True)

        # --- Mirage ---
        st.markdown('<div class="phenomenon-card">', unsafe_allow_html=True)
        st.markdown('<div class="phenomenon-title" style="color:#ffc857">🏜️ السراب — Mirage</div>')

        mirage_html = get_mirage_html()
        components.html(mirage_html, height=450)

        st.markdown("""
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:12px'>
            <div class='condition-box'>
                <div class='cond-title'>السراب الصحراوي (Inferior Mirage)</div>
                <ul>
                    <li>سطح الأرض ساخن جدًّا → الهواء الملامس أسخن</li>
                    <li>كلما ارتفعنا: تقل الحرارة ↑ ويزداد معامل الانكسار ↑</li>
                    <li>n₄ > n₃ > n₂ > n₁ (من الأعلى للأسفل)</li>
                    <li>تنكسر الأشعة مبتعدة عن العمود (نحو الأسفل)</li>
                    <li>عندما θ₁ > θc بين طبقتين: تنعكس انعكاسًا كليًّا داخليًّا</li>
                    <li>يرى المراقب صورة مقلوبة للجسم (بركة ماء)</li>
                </ul>
            </div>
            <div class='condition-box'>
                <div class='cond-title'>السراب القطبي (Superior Mirage)</div>
                <ul>
                    <li>سطح الأرض بارد جدًّا → الهواء الملامس أبرد</li>
                    <li>كلما ارتفعنا: تزداد الحرارة ↑ ويقل معامل الانكسار ↓</li>
                    <li>n₁ > n₂ > n₃ > n₄ (من الأعلى للأسفل)</li>
                    <li>تنكسر الأشعة مبتعدة عن العمود (نحو الأعلى)</li>
                    <li>عندما θ₁ > θc: انعكاس كلي داخلي</li>
                    <li>يرى المراقب صورة مقلوبة معلّقة في الأعلى</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # --- Rainbow ---
        st.markdown('<div class="phenomenon-card">', unsafe_allow_html=True)
        st.markdown('<div class="phenomenon-title" style="color:#ff4488">🌈 قوس المطر — Rainbow</div>')

        rainbow_html = get_rainbow_html()
        components.html(rainbow_html, height=490)

        st.markdown("""
        <div class='condition-box'>
            <div class='cond-title'>آلية تكوّن قوس المطر</div>
            <ul>
                <li>يسقط ضوء الشمس الأبيض على قطرة مطر في الهواء</li>
                <li><b>عند النقطة A:</b> ينكسر الضوء مقتربًا من العمود (دخول من الهواء إلى الماء) — يتحلل إلى ألوان الطيف لأن لكل لون معامل انكسار مختلف</li>
                <li><b>عند النقطة B:</b> يسقط الضوء على السطح الداخلي بزاوية أكبر من الزاوية الحرجة للماء (48.6°) → يحدث <b style='color:#ff2244'>انعكاس كلي داخلي</b></li>
                <li><b>عند النقطة C:</b> ينكسر الضوء مبتعدًا عن العمود (خروج من الماء إلى الهواء) — بزوايا مختلفة لكل لون</li>
                <li>البنفسجي: أكبر زاوية انكسار (n = 1.342) | الأحمر: أقل زاوية انكسار (n = 1.331)</li>
                <li>يُرى القوس باتجاه معاكس للشمس (الشمس من خلف المراقب)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # --- Optical Fibers ---
        st.markdown('<div class="phenomenon-card">', unsafe_allow_html=True)
        st.markdown('<div class="phenomenon-title" style="color:#00b8ff">🔗 الألياف الضوئية — Optical Fibers</div>')

        fiber_html = get_fiber_html()
        components.html(fiber_html, height=450)

        st.markdown("""
        <div style='display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:12px'>
            <div class='condition-box'>
                <div class='cond-title'>البنية والمبدأ</div>
                <ul>
                    <li>أنابيب رفيعة من الزجاج أو البلاستيك (قطر 10-50 ميكرومتر)</li>
                    <li>تتكوّن من <b style='color:#00b8ff'>القلب</b> (معامل انكسار أكبر) و<b style='color:#88aacc'>الغلاف</b> (معامل انكسار أقل)</li>
                    <li>n(قلب) > n(غلاف) ← شرط TIR متحقّق دائمًا</li>
                    <li>يسقط الضوء بزاوية أكبر من θc على الحد الفاصل بين القلب والغلاف</li>
                    <li>ينعكس انعكاسًا كليًّا داخليًّا → ينتقل الضوء مسافات طويلة دون ضياع</li>
                    <li>يمكن ثني الليف دون تأثير على الكفاءة</li>
                </ul>
            </div>
            <div class='condition-box'>
                <div class='cond-title'>التطبيقات</div>
                <ul>
                    <li><b style='color:#00e5a0'>الطب:</b> المنظار الجراحي — تنظير القولون والمفاصل والأوعية الدموية</li>
                    <li><b style='color:#00e5a0'>الطب:</b> العمليات بالمنظار — إزالة الأورام والزوائد اللحمية</li>
                    <li><b style='color:#00e5a0'>الاتصالات:</b> نقل إشارات الهاتف والإنترنت بكفاءة عالية</li>
                    <li><b style='color:#00e5a0'>الاتصالات:</b> سرية عالية ومقاومة للتشويش</li>
                    <li>ليف بسمك شعرة الإنسان ينقل ~32000 مكالمة صوتية في آن واحد!</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # --- Diamond ---
        st.markdown('<div class="phenomenon-card">', unsafe_allow_html=True)
        st.markdown('<div class="phenomenon-title" style="color:#ccccff">💎 بريق الماس</div>')
        st.markdown("""
        <div class='condition-box'>
            <div class='cond-title'>لماذا يتلألأ الماس بشكل استثنائي؟</div>
            <ul>
                <li>معامل انكسار الماس مرتفع جدًّا: <b style='direction:ltr;display:inline-block'>n = 2.42</b></li>
                <li>الزاوية الحرجة للماس صغيرة جدًّا: <b style='direction:ltr;display:inline-block'>θc = 24.4°</b></li>
                <li>أي ضوء يدخل الماس بزاوية سقوط > 24.4° ينعكس كليًّا داخليًّا</li>
                <li>يُصمَّم الماس بأوجه متعددة بحيث يدخل الضوء ويتكرر الانعكاس الكلي الداخلي عدة مرات</li>
                <li>يتركّز الضوء في أماكن معينة ويخرج منها → ظهور الماس متلألئًا</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================
    #  TAB 6: ASSESSMENT
    # ========================================================
    with tabs[5]:
        st.markdown('<div class="section-title"><span class="icon">✅</span> تقويم فهم الدرس</div>', unsafe_allow_html=True)

        if "quiz_answers" not in st.session_state:
            st.session_state.quiz_answers = {}
        if "quiz_score" not in st.session_state:
            st.session_state.quiz_score = None

        quiz_data = [
            {
                "q": "ما المقصود بالزاوية الحرجة؟",
                "opts": [
                    "أ) زاوية السقوط التي تنعدم فيها زاوية الانكسار",
                    "ب) زاوية الانكسار التي يساوي عندها معامل الانكسار 1",
                    "ج) زاوية السقوط التي تكون عندها زاوية الانكسار تساوي 90°",
                    "د) زاوية الانعكاس التي تساوي فيها زاوية السقوط"
                ],
                "correct": 2,
                "explain": "الزاوية الحرجة هي زاوية السقوط في الوسط الأكثف التي يكون عندها الشعاع المنكسر ملامسًا للحد الفاصل بين الوسطين (θ₂ = 90°)."
            },
            {
                "q": "أيٌّ ممّا يلي ليس من شروط حدوث الانعكاس الكلي الداخلي؟",
                "opts": [
                    "أ) أن ينتقل الضوء من وسط أكثف إلى أقل كثافة",
                    "ب) أن تكون زاوية السقوط أكبر من الزاوية الحرجة",
                    "ج) أن يكون معامل انكسار الوسط الثاني أكبر من الأول",
                    "د) أن تكون زاوية السقوط مساوية لزاوية الانعكاس"
                ],
                "correct": 2,
                "explain": "الشرط هو n₁ > n₂ وليس n₂ > n₁. إذا كان n₂ > n₁ فالضوء ينتقل من أقل كثافة إلى أكثف ولا يمكن حدوث TIR."
            },
            {
                "q": "إذا كان معامل انكسار الماس 2.42، فما زاويته الحرجة؟ (الوسط الثاني هو الهواء)",
                "opts": [
                    "أ) 41.8°",
                    "ب) 48.6°",
                    "ج) 24.4°",
                    "د) 60.0°"
                ],
                "correct": 2,
                "explain": "sin θc = 1/n = 1/2.42 = 0.4132 → θc = arcsin(0.4132) = 24.4°"
            },
            {
                "q": "سقط شعاع ضوئي من الزجاج (n=1.5) إلى الهواء بزاوية سقوط 30°. ماذا يحدث؟ (θc للزجاج = 41.8°)",
                "opts": [
                    "أ) انعكاس كلي داخلي",
                    "ب) انكسار بزاوية أكبر من 30°",
                    "ج) انكسار بزاوية أقل من 30°",
                    "د) يمر الشعاع دون تغيير"
                ],
                "correct": 1,
                "explain": "θ₁ = 30° < θc = 41.8° → ينكسر الشعاع مبتعدًا عن العمود. sin θ₂ = 1.5 × sin(30°) / 1 = 0.75 → θ₂ = 48.6° (أكبر من 30°)."
            },
            {
                "q": "في قوس المطر، أين يحدث الانعكاس الكلي الداخلي؟",
                "opts": [
                    "أ) عند دخول الضوء إلى قطرة المطر",
                    "ب) عند خروج الضوء من قطرة المطر",
                    "ج) على السطح الداخلي الخلفي لقطرة المطر",
                    "د) في الهواء بين القطرة والمراقب"
                ],
                "correct": 2,
                "explain": "بعد دخول الضوء إلى القطرة وانكساره، يسقط على السطح الداخلي الخلفي بزاوية أكبر من θc للماء (48.6°) فينعكس انعكاسًا كليًّا داخليًّا، ثم ينكسر مرة أخرى عند الخروج."
            },
            {
                "q": "لماذا لا يمكن حدوث الانعكاس الكلي الداخلي عند انتقال الضوء من الهواء إلى الماء؟",
                "opts": [
                    "أ) لأن الماء معتم",
                    "ب) لأن n(H₂O) < n(air)",
                    "ج) لأن n(H₂O) > n(air) أي الضوء ينتقل من أقل كثافة إلى أكثف",
                    "د) لأن الزاوية الحرجة للماء صفر"
                ],
                "correct": 2,
                "explain": "يشترط لحدوث TIR أن ينتقل الضوء من وسط أكثف إلى أقل كثافة (n₁ > n₂). عند الانتقال من الهواء (n=1) إلى الماء (n=1.33) نجد n₁ < n₂ فلا يمكن حدوث TIR."
            },
            {
                "q": "إذا كانت الزاوية الحرجة لمادة شفافة تساوي 45°، فما معامل انكسارها؟ (الوسط الثاني هو الهواء)",
                "opts": [
                    "أ) 1.00",
                    "ب) 1.41",
                    "ج) 1.50",
                    "د) 2.00"
                ],
                "correct": 1,
                "explain": "sin θc = 1/n → sin(45°) = 1/n → 0.7071 = 1/n → n = 1/0.7071 = 1.414 ≈ 1.41"
            },
            {
                "q": "ما الظاهرة التي تفسر رؤية بركة ماء في الصحراء وهي في الحقيقة ليست موجودة؟",
                "opts": [
                    "أ) الانعراج",
                    "ب) التداخل",
                    "ج) السراب الصحراوي (انكسارات متتالية + TIR)",
                    "د) الاستقطاب"
                ],
                "correct": 2,
                "explain": "السراب الصحراوي يحدث بسبب انكسارات متتالية لأشعة الضوء في طبقات الهواء ذات درجات الحرارة المختلفة، وعندما تزيد زاوية السقوط عن الزاوية الحرجة بين طبقتين متجاورتين يحدث انعكاس كلي داخلي."
            }
        ]

        score = 0
        total = len(quiz_data)

        for qi, q in enumerate(quiz_data):
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(f"**س{qi+1}. {q['q']}**")

            selected = st.radio(
                "", q["opts"], index=None,
                key=f"quiz_{qi}",
                label_visibility="collapsed"
            )

            if selected is not None:
                st.session_state.quiz_answers[qi] = selected
                sel_idx = q["opts"].index(selected)
                if sel_idx == q["correct"]:
                    st.markdown("<span class='result-badge' style='background:rgba(0,229,160,0.15);border:1px solid rgba(0,229,160,0.4);color:#00e5a0'>✓ إجابة صحيحة</span>", unsafe_allow_html=True)
                else:
                    correct_text = q["opts"][q["correct"]]
                    st.markdown(f"<span class='result-badge badge-tir'>✗ إجابة خاطئة — الصحيح: {correct_text}</span>", unsafe_allow_html=True)
                st.markdown(f"<div style='color:#7a8ba8;font-size:0.85rem;margin-top:6px;padding:8px 12px;background:rgba(255,255,255,0.03);border-radius:6px'>{q['explain']}</div>", unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

        answered = len(st.session_state.quiz_answers)
        if answered > 0:
            for qi, q in enumerate(quiz_data):
                if qi in st.session_state.quiz_answers:
                    sel_idx = q["opts"].index(st.session_state.quiz_answers[qi])
                    if sel_idx == q["correct"]:
                        score += 1

        st.markdown("---")
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("📊 عرض النتيجة", type="primary", use_container_width=True):
                st.session_state.quiz_score = score
        with btn_col2:
            if st.button("🔄 إعادة المحاولة", use_container_width=True):
                st.session_state.quiz_answers = {}
                st.session_state.quiz_score = None
                st.rerun()

        if st.session_state.quiz_score is not None:
            pct = (st.session_state.quiz_score / total) * 100
            if pct >= 80:
                color = "#00e5a0"
                msg = "ممتاز! فهمك للدرس رائع 🌟"
            elif pct >= 60:
                color = "#ffc857"
                msg = "جيد! لكن هناك بعض النقاط التي تحتاج مراجعة 📖"
            elif pct >= 40:
                color = "#ff8844"
                msg = "مقبول. راجع الدرس وحاول مرة أخرى 📝"
            else:
                color = "#ff2244"
                msg = "يحتاج تحسين. راجع الدرس بعناية ثم عد للمحاولة 📚"

            st.markdown(f"""
            <div style='background:rgba(13,21,37,0.9);border:1px solid {color}33;border-radius:14px;padding:24px;text-align:center;margin-top:8px'>
                <div style='font-size:2.5rem;font-weight:900;color:{color};direction:ltr'>
                    {st.session_state.quiz_score} / {total}
                </div>
                <div style='font-size:1.1rem;color:#e8ecf4;margin:8px 0'>{msg}</div>
                <div style='font-size:0.9rem;color:#7a8ba8'>النسبة: {pct:.0f}% | أجبت على {answered} من {total} أسئلة</div>
            </div>
            """, unsafe_allow_html=True)


# ============================================================
#  RUN
# ============================================================
if __name__ == "__main__":
    main()
