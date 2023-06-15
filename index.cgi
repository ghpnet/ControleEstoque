#!/usr/bin/perl
print "Content-type: text/html\n\n";
use CGI;
$cgi = new CGI;
$acao = $cgi->param("acao");
print qq~
<!DOCTYPE html>
<html lang="pt-br">
<head>
<title>TECNOMARC ::.. Controle de estoque</title>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style type="text/css">td img {display: block;}</style>
<link rel="stylesheet" type="text/css" href="estilo.css">

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


<body>
    <div class="container">
	<!--
            <li><a href="?acao=os_cad">Cadastrar nova OS</a></li>
            <li><a href="?acao=os_aberta">Listar O.S em aberto</a></li>
            <li><a href="?acao=os_fechadas">Listar O.S enceradas</a></li>
            <li><a href="?acao=os_buscar">Buscar O.S</a></li>
            <li><a href="?acao=pecas">Peças e Serviços</a></li>
            <li><a href="?acao=caixa">Caixa</a></li>
	-->
      <div class="row">
        <div class="col-sm-6">
          <br><img src="logo.png" alt="uvas" class="img-responsive">
        </div>
	</div>
<br>
</div>

    <!-- Barra Navegação -->
    <nav class="navbar navbar-default">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#barra-navegacao">
            <span class="sr-only">Alternar Menu</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a href="#" class="navbar-brand">Opções do sistema</a>
        </div>

        <div id="barra-navegacao" class="collapse navbar-collapse">
          <ul class="nav navbar-nav navbar-right">

            <li><a href="./?acao=inicial">Página Inicial</a></li>
            <li><a href="./?acao=inicial">NOVA VENDA</a></li>
            <li><a href="./?acao=novo">Inventário</a></li>
            <li><a href="./?acao=novo">Fornecedor</a></li>
            <li><a href="./?acao=clientes">Clientes</a></li>

            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Produtos<span class="caret"></span>
            </a>
              <ul class="dropdown-menu">
                <li><a href="./?acao=novoprod">Cadastrar Proutos</a></li>
                <li><a href="./?acao=clientes">Entradas</a></li>
		<li><a href="./?acao=novocliente">saidas</a></li>
              </ul>
            </li>

		<li><a href="./?acao=relmensal">Relátorio</a></li>

	</div>

      </div>
    </nav>

<div class="container">
~;
###############################
if($acao eq "inicial"){
print qq~
Olá, hoje é --DIA--<br>
Utilze uma das opções do menu acima!
<br><br>
Produto com baixo estoque<br>
Nenhum produto com baixo estoque no momento.
~;

}
###############################
if($acao eq "novoprod"){
print qq~
<form method="POST" name="novoprod">
Titulo: <input type="text" name="titulo"><br>
Referencia: <input type="text" name="referencia"><br>
Descrição: <input type="text" name="descricao"><br>
Fornecedor: <input type="text" name="fornecedor"><br>
Unidade de consumo: <input type="text" name="unidade"><br>
Estoque Mínimo: <input type="text" name="minimo"><br>
Estoque atual: <input type="text" name="atual"><br>
Custo Unítario: R\$ <input type="text" name="custo"><br>
Valor de venda: R\$ <input type="text" name="valor"><br>
<input type="submit" name="btn_cad" value="Cadastrar Produto">
<input type="hidden" name="acao" value="novoprod2">
</form>
~;
}
##############################
if($acao eq "novoprod2"){
$id = time;
$titulo = $cgi->param("titulo");
$referencia = $cgi->param("referencia");
$descricao = $cgi->param("descricao");
$fornecedor = $cgi->param("fornecedor");
$unidade = $cgi->param("unidade");
$minimo = $cgi->param("minimo");
$atual = $cgi->param("atual");
$custo = $cgi->param("custo");
$valor = $cgi->param("valor");

open(PROD,">>produtos.dat");
print PROD "$id|$titulo|$referencia|$descricao|$fornecedor|$unidade|$minimo|$atual|$custo|$valor\n";
close(PROD);

print qq~
<h4>Produto cadastrado com sucesso!</h4><br><br>
Titulo: $titulo<br>
Referencia: $referencia<br>
Descrição: $descricao<br>
Fornecedor: $fornecedor<br>
Unidade de consumo: $unidade<br>
Estoque Mínimo: $estoque<br>
Estoque atual: $atual<br>
Custo Unítario: R\$ $custo<br>
Valor de venda: R\$ $valor
~;
}
##############################
print qq~
</div>

<hr size="1" width="80%">
<center>TECNOMARC - 2023</center>

</body>
</html>
~;
