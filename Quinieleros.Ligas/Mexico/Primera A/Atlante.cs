using System;

namespace Quinieleros.Ligas
{
	public class Atlante : EquipoMexico
	{
		public Atlante ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los potros de hierro", "Los Azulgranas", "El équipo del pueblo" };
			this.Nombre = "Atlante";
			this.Icon = "";
			this.id = "ATLANTE";
		}
	}
}

