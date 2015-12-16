using System;

namespace Quinieleros.Ligas
{
	public class Merida : EquipoMexico
	{
		public Merida ()
		{
			this.Apodos = new System.Collections.Generic.List<string> (){ "Los Venados", "El Astado","Los Ciervos", "Los titanes del sureste" };
			this.Nombre = "Mérida";
			this.Icon = "";
			this.id = "MERIDA";
		}
	}
}

