const ENDPOINT = `ws://kucheriavyi.ru:8832/ws`
const W = window
const D = W.document

function l(n, h, o = W) { o.addEventListener(n, h) }

function ID() {
	let id = localStorage.getItem('ID') ?? ''
	if (id) {
		return id
	}

	for (let i = 0; i < 8; i++) {
		id += 'abcdef0123456789'.charAt(Math.floor(Math.random() * 16))
	}
	localStorage.setItem('ID', id)
	return id
}

class UI {
	static delay = 10

	constructor() {
		this.id = ID()
		this.root = D.getElementById('root')
		this.ctx = this.root.getContext('2d')
		this.ws = new WebSocket(ENDPOINT)

		this.listen()
		this.resize(null)
	}

	delayer = null

	listen() {
		l('click', (e) => this.click(e))
		l('mousemove', (e) => this.move(e))
		l('keypress', (e) => this.press(e))
		l('resize', (e) => this.resize(e))

		this.ws.onmessage = (e) => this.get(e)
	}

	send(event) {
		this.ws.send(JSON.stringify({
			event,
			client: { id: this.id, w: this.root.width, h: this.root.height, page: location.pathname },
		}))
	}

	sendDelayed(event) {
		if (this.delayer) {
			clearTimeout(this.delayer)
		}

		this.delayer = setTimeout(() => this.send(event), UI.delay)
	}

	get(e) {
		const img = new Image()
		const data = JSON.parse(e.data)

		img.onload = () => this.ctx.drawImage(img, data.x, data.y)
		img.src = `data:image/png;base64,${data.img}`
	}

	resize(e) {
		this.root.width = W.innerWidth
		this.root.height = W.innerHeight
		e && this.sendDelayed({ type: 'resize' })
	}

	click(e) {
		this.send({ type: 'click', x: e.clientX, y: e.clientY })
	}

	press(e) {
		this.send({ type: 'key', value: e.key })
	}

	move(e) {
		this.sendDelayed({ type: 'move', x: e.clientX, y: e.clientY })
	}
}

l('DOMContentLoaded', () => W.ui = new UI(),D)
