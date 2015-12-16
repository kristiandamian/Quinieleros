using System;

namespace Quinieleros.Ligas
{
	public class LobosBUAP:EquipoMexico
	{
		public LobosBUAP ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "La Manada","Los licántropos", "Los Lobos" };
			this.Nombre = "Lobos BUAP";
			this.Icon = "";
			this.id = "LOBOS";
		}
	}
}

