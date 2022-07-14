import java.util.Scanner;
public class jogoVelha {	
	//Cadeia de funções e métodos
	static int[] pedirJogada(int jogador) {
		int vetorJogada[] = new int[2];
		int linha, coluna;
		Scanner scanner = new Scanner(System.in);
		if (jogador == 1) {
			System.out.println("*** Jogador1 ***");
			
			System.out.print("Digite a linha do tabuleiro: ");
			linha = scanner.nextInt();		
			
			System.out.print("Digite a coluna do tabuleiro: ");
			coluna = scanner.nextInt();		
		} else {
			System.out.println("*** Jogador2 ***");
			
			System.out.print("Digite a linha do tabuleiro: ");
			linha = scanner.nextInt();

			System.out.print("Digite a coluna do tabuleiro: ");
			coluna = scanner.nextInt();
		}
		
		vetorJogada[0] = linha - 1;
		vetorJogada[1] = coluna - 1;
		
		return vetorJogada;
	}

	static void inserirNoTabuleiro(int jogador, String tabuleiro[][]) {
		int vetor[] = pedirJogada(jogador);
		if (jogador == 1) {
			while (tabuleiro[vetor[0]][vetor[1]] != ".") {
				System.out.print("Posição já ocupada, por favor tente novamente\n");
				vetor = pedirJogada(jogador);
			}
			tabuleiro[vetor[0]][vetor[1]] = "X";
		} else {
			while (tabuleiro[vetor[0]][vetor[1]] != ".") {
				System.out.print("Posição já ocupada, por favor tente novamente\n");
				vetor = pedirJogada(jogador);
			}
			tabuleiro[vetor[0]][vetor[1]] = "O";
		}
		imprimirTabuleiro(tabuleiro);
	}

	static void imprimirTabuleiro(String tabuleiro[][]) {
		for (int i = 0; i < tabuleiro.length; i++) {
			for (int j = 0; j < tabuleiro[i].length; j++) {
				System.out.print(tabuleiro[i][j]);
			}
			System.out.println();
		}
	}

	static boolean verificarVitoria(boolean ganhou, String jogador, String[][] tabuleiro) {
		//Vitória em linhas
		for (int i = 0; i < tabuleiro.length; i++) {
			if (tabuleiro[i][0].equals(jogador) && tabuleiro[i][1].equals(jogador) && tabuleiro[i][2].equals(jogador)) {
		        	ganhou = true;
			} else if (tabuleiro[0][i].equals(jogador) && tabuleiro[1][i].equals(jogador) && tabuleiro[2][i].equals(jogador)) {
				ganhou = true;
			}
		}
		//Vitória em diagonais
		if (tabuleiro[0][0].equals(jogador) && tabuleiro[1][1].equals(jogador) && tabuleiro[2][2].equals(jogador)) {
			ganhou = true;
		} else if (tabuleiro[2][0].equals(jogador) && tabuleiro[1][1].equals(jogador) && tabuleiro[0][2].equals(jogador)) {
			 ganhou = true;
		}
		return ganhou;
	}	

	static boolean verificarSeTabuleiroEstaCheio(boolean estaCheio, String tabuleiro[][]) {
		int i = 0;
		int j = 0;
		for (i = 0; i < tabuleiro.length; i++) {
			for (j = 0; j < tabuleiro[i].length; j++) {
				tabuleiro[i][j].equals(".");
				break;
			}
		} 
		if ((j == 2 && i == 2) && (tabuleiro[i][j].equals(".") == false)) {
			estaCheio = true;
		}
		return estaCheio;
	}	

	//Método principal
	public static void main(String[] args) {
		boolean ganhou = false;
		boolean estaCheio = false;
		String vencedor = "nenhum";
		String tabuleiro[][] = new String[3][3];

		for (int i = 0; i < tabuleiro.length; i++) {
			for (int j = 0; j < tabuleiro[i].length; j++) {
				tabuleiro[i][j] = ".";
			}
		}
		
		imprimirTabuleiro(tabuleiro);
		while (ganhou == false || estaCheio == false) {
			//Jogador1 "X"
			estaCheio = verificarSeTabuleiroEstaCheio(estaCheio, tabuleiro);
			inserirNoTabuleiro(1, tabuleiro);
			ganhou = verificarVitoria(ganhou ,"X", tabuleiro);
			if (ganhou == true) {
				vencedor = "Jogador1";
				break;
			}
			//Jogador 2 "O"	
			estaCheio = verificarSeTabuleiroEstaCheio(estaCheio, tabuleiro);
			inserirNoTabuleiro(2, tabuleiro);
			ganhou = verificarVitoria(ganhou, "O", tabuleiro);
			if (ganhou == true) {
				vencedor = "jogador2";
				break;
			}
		}
		System.out.println("Jogo finalizado");
		if (vencedor.equals("nenhum") == false) {
			System.out.println(vencedor + " venceu!!!");
		} else {
			System.out.println("Deu velha, não houve vencedores");
		}
	}
}




