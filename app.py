from py2neo import Graph
from flask import Flask, render_template


graph = Graph(password='1234')
app = Flask(__name__, template_folder='templates')


class Object(object):
    pass


@app.route('/')
def index_page():
    results = graph.run(
        'MATCH (c:Caracteristica) OPTIONAL MATCH (c:Caracteristica)<-[:POSSUI]-(p:Postagem)-[:CONVERTEU_EM]->('
        'v:Venda) RETURN c.descricao as descricao, sum(v.valor) as valor_total, count(distinct v) as vendas, '
        'count(distinct p) as publicacoes, coalesce(round(avg(v.valor)), 0) as media, c.identificador as id ORDER BY '
        'media DESC')
    return render_template('index.html', results=results)


@app.route('/posts/<characteristic>')
def characteristic_page(characteristic):
    results = graph.run('MATCH (v:Venda)<-[:CONVERTEU_EM]-(p:Postagem)-[:POSSUI]->(c:Caracteristica{identificador:{'
                        'id}}) RETURN p, v, c ORDER BY v.id DESC', {'id': characteristic})
    results = results.data()
    sales = []
    posts = []
    char = None
    for p in results:
        char = p['c']
        p['v']['cid'] = p['p']['identificador']
        p['p']['total'] = (p['p']['total'] if p['p']['total'] else 0) + p['v']['valor']
        if p['p'] not in posts:
            posts.append(p['p'])
        sales.append(p['v'])

    return render_template('characteristics.html', posts=posts, sales=sales, char=char)


if __name__ == '__main__':
    app.run()
