import java.util.Scanner;

public class acessibilidade {
	
	public static void main(String[] args){
			
		Scanner ler = new Scanner(System.in);
		float H, C, L, i;
		String saida="";
		
		do{
			String entrada = ler.nextLine();
			String[] vetor = entrada.split(" ");
			H = Float.parseFloat(vetor[0]);
			C = Float.parseFloat(vetor[1]);
			L = Float.parseFloat(vetor[2]);
			
			if(H > 0 && C > 0 && L > 0){

				i = (H*100)/C;
				
				if(i <= 8.334 && L>= 0.80){
					saida += "PROJETO SIMPLES\n";
				}else if(i <= 8.334 || L>= 0.80) {
					saida += "PROJETO ESPECIAL\n";
				}
			}
		}while(H!=0.0 && C!=0.0 && L!=0.0);
		System.out.print(saida);
	}
}
